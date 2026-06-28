// Kiểm tra xem người dùng đã chọn ít nhất 1 triệu chứng chưa trước khi submit
function validateForm() {
    const checkboxes = document.querySelectorAll('input[name="symptoms"]:checked');
    const errorMsg = document.getElementById('error-msg');
    
    if (checkboxes.length === 0) {
        errorMsg.textContent = "Vui lòng chọn ít nhất 1 triệu chứng để chẩn đoán!";
        return false;
    }
    
    errorMsg.textContent = "";
    return true;
}
