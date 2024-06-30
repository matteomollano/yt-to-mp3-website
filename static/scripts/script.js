const coverArtSelect = document.querySelector('.form-select');
const customCoverArtInput = document.querySelector('.custom-cover-art-input');

coverArtSelect.addEventListener('change', () => {
    if (coverArtSelect.value === 'custom-cover-art') {
        customCoverArtInput.style.display = 'block';
    } else {
        customCoverArtInput.style.display = 'none';
    }
});

const fileInput = document.querySelector('#custom-cover-art-file');
const fileSelectedSpan = document.querySelector('#file-selected');

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        const fileName = fileInput.files[0].name;
        fileSelectedSpan.textContent = fileName;
    } else {
        fileSelectedSpan.textContent = '';
    }
});