"# expert_system/rules.py

# Tập luật IF-THEN mở rộng (9 bệnh lý hô hấp phổ biến)
# ""conditions"" là toàn bộ tập triệu chứng đặc trưng của bệnh.
# Hệ thống sẽ tính % khả năng mắc bệnh = (số triệu chứng người dùng chọn
# có trong ""conditions"") / (tổng số triệu chứng trong ""conditions"") * 100
RULES = [
    {
        ""conditions"": [""Sốt"", ""Ho"", ""Khó thở""],
        ""disease"": ""Viêm phổi""
    },
    {
        ""conditions"": [""Ho kéo dài"", ""Khò khè""],
        ""disease"": ""Hen suyễn""
    },
    {
        ""conditions"": [""Đau họng"", ""Chảy nước mũi""],
        ""disease"": ""Viêm đường hô hấp trên""
    },
    {
        ""conditions"": [""Ho"", ""Đờm nhiều"", ""Đau ngực""],
        ""disease"": ""Viêm phế quản""
    },
    {
        ""conditions"": [""Sốt"", ""Ho"", ""Mệt mỏi"", ""Đau cơ""],
        ""disease"": ""Cúm (Influenza)""
    },
    {
        ""conditions"": [""Ho kéo dài"", ""Sốt"", ""Sụt cân"", ""Đau ngực""],
        ""disease"": ""Lao phổi""
    },
    {
        ""conditions"": [""Khó thở"", ""Ho kéo dài"", ""Đờm nhiều""],
        ""disease"": ""Bệnh phổi tắc nghẽn mạn tính (COPD)""
    },
    {
        ""conditions"": [""Chảy nước mũi"", ""Hắt hơi"", ""Ngứa mũi"", ""Nghẹt mũi""],
        ""disease"": ""Viêm mũi dị ứng""
    },
    {
        ""conditions"": [""Khản tiếng"", ""Đau họng"", ""Ho""],
        ""disease"": ""Viêm thanh quản""
    }
]

# Kho tri thức Y tế: Xét nghiệm và Điều trị tương ứng
MEDICAL_KNOWLEDGE = {
    ""Viêm phổi"": {
        ""tests"": [""X-quang phổi thẳng"", ""Công thức máu (CBC)"", ""Định lượng CRP""],
        ""treatments"": [""Sử dụng kháng sinh theo đơn bác sĩ"", ""Nghỉ ngơi tuyệt đối"", ""Bù nước và điện giải""]
    },
    ""Hen suyễn"": {
        ""tests"": [""Đo chức năng hô hấp (Hô hấp ký)"", ""Test phục hồi phế quản""],
        ""treatments"": [""Sử dụng thuốc giãn phế quản dạng xịt/hít"", ""Tránh các tác nhân gây dị ứng"", ""Theo dõi lưu lượng đỉnh kế""]
    },
    ""Viêm đường hô hấp trên"": {
        ""tests"": [""Nội soi tai mũi họng"", ""Sàng lọc nhanh virus""],
        ""treatments"": [""Súc họng bằng nước muối sinh lý"", ""Sử dụng thuốc giảm đau, hạ sốt khi cần"", ""Tăng cường vitamin C""]
    },
    ""Viêm phế quản"": {
        ""tests"": [""Xét nghiệm vi sinh đờm"", ""X-quang ngực thẳng""],
        ""treatments"": [""Sử dụng thuốc long đờm"", ""Uống nhiều nước ấm"", ""Hạn chế tiếp xúc khói thuốc, bụi bẩn""]
    },
    ""Cúm (Influenza)"": {
        ""tests"": [""Test nhanh Cúm A/B"", ""Real-time PCR (nếu có biến chứng)""],
        ""treatments"": [""Dùng thuốc kháng virus (như Oseltamivir) trong 48h đầu nếu có chỉ định"", ""Hạ sốt bằng Paracetamol"", ""Cách ly giảm lây nhiễm""]
    },
    ""Lao phổi"": {
        ""tests"": [""Nhuộm soi đờm tìm AFB"", ""Chụp X-quang phổi"", ""Xét nghiệm KRISTeller/GeneXpert""],
        ""treatments"": [""Điều trị bằng phác đồ chống lao chuẩn (đúng - đủ - đều)"", ""Nâng cao dinh dưỡng, bổ sung đạm"", ""Theo dõi chức năng gan, thận""]
    },
    ""Bệnh phổi tắc nghẽn mạn tính (COPD)"": {
        ""tests"": [""Đo chức năng hô hấp"", ""Khí máu động mạch (khi trở nặng)"", ""Chụp CT ngực độ phân giải cao""],
        ""treatments"": [""Sử dụng thuốc giãn phế quản tác dụng kéo dài (LABA/LAMA)"", ""Cai thuốc lá/thuốc lào tuyệt đối"", ""Tập phục hồi chức năng hô hấp""]
    },
    ""Viêm mũi dị ứng"": {
        ""tests"": [""Test áp da với dị nguyên"", ""Định lượng IgE đặc hiệu trong máu""],
        ""treatments"": [""Sử dụng thuốc kháng histamin (viên uống)"", ""Xịt mũi Corticoid theo hướng dẫn"", ""Rửa mũi bằng nước muối biển""]
    },
    ""Viêm thanh quản"": {
        ""tests"": [""Nội soi thanh quản ống mềm""],
        ""treatments"": [""Hạn chế nói chuyện, giữ ấm cổ họng"", ""Xông mũi họng bằng tinh dầu"", ""Dùng thuốc kháng viêm, giảm phù nề nhẹ""]
    }
}
"
