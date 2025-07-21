// Modal functionality
function openModal(imageSrc, digit, confidence) {
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImage');
    const modalDigit = document.getElementById('modalDigit');
    const modalConfidence = document.getElementById('modalConfidence');
    
    modal.style.display = 'block';
    modalImg.src = imageSrc;
    modalDigit.textContent = digit;
    modalConfidence.textContent = confidence;
}

// Close modal functionality
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('imageModal');
    const closeBtn = document.getElementsByClassName('close')[0];
    
    // Close modal when clicking the X
    closeBtn.onclick = function() {
        modal.style.display = 'none';
    }
    
    // Close modal when clicking outside of it
    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    }
    
    // Close modal with Escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            modal.style.display = 'none';
        }
    });
});