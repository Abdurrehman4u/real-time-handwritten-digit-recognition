document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('drawingCanvas');
    const ctx = canvas.getContext('2d');
    const predictBtn = document.getElementById('predictBtn');
    const clearBtn = document.getElementById('clearBtn');
    const uploadBtn = document.getElementById('uploadBtn');
    const imageUpload = document.getElementById('imageUpload');
    const predictedDigitSpan = document.getElementById('predictedDigit');
    const confidenceSpan = document.getElementById('confidenceScore');
    const predictionIdSpan = document.getElementById('predictionId');
    const inputImage = document.getElementById('inputImage');
    const viewHistoryBtn = document.getElementById('viewHistoryBtn');

    let isDrawing = false;

    // Set up canvas for drawing
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 15;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    clearCanvas(); // Initialize with black background

    // Mouse events for drawing on canvas
    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDrawing);
    canvas.addEventListener('mouseout', stopDrawing);

    // Touch events for mobile devices
    canvas.addEventListener('touchstart', handleTouch);
    canvas.addEventListener('touchmove', handleTouch);
    canvas.addEventListener('touchend', stopDrawing);

    function startDrawing(e) {
        isDrawing = true;
        const rect = canvas.getBoundingClientRect();
        const x = (e.clientX || e.touches[0].clientX) - rect.left;
        const y = (e.clientY || e.touches[0].clientY) - rect.top;
        ctx.beginPath();
        ctx.moveTo(x, y);
    }

    function draw(e) {
        if (!isDrawing) return;
        
        const rect = canvas.getBoundingClientRect();
        const x = (e.clientX || e.touches[0].clientX) - rect.left;
        const y = (e.clientY || e.touches[0].clientY) - rect.top;
        
        ctx.lineTo(x, y);
        ctx.stroke();
    }

    function stopDrawing() {
        if (isDrawing) {
            isDrawing = false;
            ctx.beginPath();
        }
    }

    function handleTouch(e) {
        e.preventDefault();
        const touch = e.touches[0];
        const mouseEvent = new MouseEvent(e.type === 'touchstart' ? 'mousedown' : 
                                        e.type === 'touchmove' ? 'mousemove' : 'mouseup', {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        canvas.dispatchEvent(mouseEvent);
    }

    // Clear canvas function
    function clearCanvas() {
        ctx.fillStyle = 'black';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        predictedDigitSpan.textContent = '-';
        confidenceSpan.textContent = '-';
        predictionIdSpan.textContent = '-';
        inputImage.style.display = 'none';
    }

    // Clear button event listener
    clearBtn.addEventListener('click', clearCanvas);

    // Predict from canvas drawing
    predictBtn.addEventListener('click', function() {
        const canvasData = canvas.toDataURL('image/png');
        
        $.ajax({
            url: '/predict',
            type: 'POST',
            data: {
                canvas_data: canvasData
            },
            success: function(response) {
                if (response.prediction) {
                    predictedDigitSpan.textContent = response.prediction;
                    confidenceSpan.textContent = response.confidence;
                    predictionIdSpan.textContent = response.id;
                    // Show the canvas as input image
                    inputImage.src = canvasData;
                    inputImage.style.display = 'block';
                } else if (response.error) {
                    alert('Error: ' + response.error);
                }
            },
            error: function() {
                alert('Error occurred during prediction');
            }
        });
    });

    // Handle file upload
    uploadBtn.addEventListener('click', function() {
        const file = imageUpload.files[0];
        if (!file) {
            alert('Please select an image file first!');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        $.ajax({
            url: '/predict',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response.prediction) {
                    predictedDigitSpan.textContent = response.prediction;
                    confidenceSpan.textContent = response.confidence;
                    predictionIdSpan.textContent = response.id;
                    // Show the uploaded image
                    inputImage.src = '/' + response.image_path;
                    inputImage.style.display = 'block';
                } else if (response.error) {
                    alert('Error: ' + response.error);
                }
            },
            error: function() {
                alert('Error occurred during prediction');
            }
        });
    });

    // Preview uploaded image
    imageUpload.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                inputImage.src = e.target.result;
                inputImage.style.display = 'block';
                predictedDigitSpan.textContent = '-';
                confidenceSpan.textContent = '-';
                predictionIdSpan.textContent = '-';
            };
            reader.readAsDataURL(file);
        }
    });

    // Navigate to history page - THIS IS THE KEY PART
    viewHistoryBtn.addEventListener('click', function() {
        console.log('History button clicked!'); // Debug log
        window.location.href = '/history';
    });
});