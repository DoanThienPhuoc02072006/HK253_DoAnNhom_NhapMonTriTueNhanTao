def forward_chaining(facts, rules, min_match_ratio=0.0):
    """
    Thuật toán suy diễn tiến có tính % khả năng mắc bệnh.

    Vì nhiều bệnh hô hấp có triệu chứng trùng lặp với nhau, thay vì chỉ
    trả về bệnh "khớp đủ 100% điều kiện" như suy diễn tiến cổ điển,
    hàm này tính độ phù hợp (matching score) của TẤT CẢ các bệnh có
    trong tập luật, dựa trên công thức:

        % khả năng = (số triệu chứng người dùng có, trùng với
                      triệu chứng đặc trưng của bệnh)
                     / (tổng số triệu chứng đặc trưng của bệnh) * 100

    - facts: Danh sách các triệu chứng đầu vào (do bệnh nhân chọn).
    - rules: Tập luật IF-THEN, mỗi luật có "conditions" (list triệu chứng)
      và "disease" (tên bệnh).
    - min_match_ratio: Ngưỡng tỉ lệ khớp tối thiểu (0.0 - 1.0) để bệnh
      được đưa vào kết quả. Mặc định = 0.0 (chỉ cần khớp >= 1
      triệu chứng cũng được liệt kê, để bệnh nhân thấy đầy đủ
      các khả năng, dù thấp).

    Trả về: list các dict đã sắp xếp giảm dần theo "probability":
        [
            {
                "disease": "Viêm phổi",
                "matched_symptoms": ["Sốt", "Ho"],
                "total_symptoms": 3,
                "matched_count": 2,
                "probability": 66.67
            },
            ...
        ]
    """
    fact_set = set(facts)
    results = []

    for rule in rules:
        conditions = rule["conditions"]
        total = len(conditions)
        if total == 0:
            continue

        matched = [c for c in conditions if c in fact_set]
        matched_count = len(matched)

        if matched_count == 0:
            continue  # Bệnh không liên quan gì đến triệu chứng đã chọn

        ratio = matched_count / total
        if ratio < min_match_ratio:
            continue

        results.append({
            "disease": rule["disease"],
            "matched_symptoms": matched,
            "total_symptoms": total,
            "matched_count": matched_count,
            "probability": round(ratio * 100, 2)
        })

    # Sắp xếp từ % khả năng cao xuống thấp.
    # Khi % bằng nhau, bệnh có nhiều triệu chứng khớp hơn (matched_count)
    # được ưu tiên xếp trước, vì độ tin cậy cao hơn.
    results.sort(
        key=lambda r: (r["probability"], r["matched_count"]),
        reverse=True
    )

    return results
