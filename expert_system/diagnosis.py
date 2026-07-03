from expert_system.rules import RULES, MEDICAL_KNOWLEDGE
from expert_system.forward_chaining import forward_chaining


def run_diagnosis(symptoms):
    """
    Chạy suy diễn tiến và trả về danh sách bệnh kèm % khả năng mắc,
    đã sắp xếp giảm dần theo xác suất, cùng các xét nghiệm/điều trị
    tổng hợp tương ứng.
    """
    ranked_diseases = forward_chaining(symptoms, RULES)

    if not ranked_diseases:
        return {
            "diseases": [],
            "no_result_message": "Không xác định rõ bệnh lý (Cần thăm khám trực tiếp để chẩn đoán thêm)",
            "tests": [],
            "treatments": []
        }

    tests = []
    treatments = []

    for item in ranked_diseases:
        disease_name = item["disease"]
        if disease_name in MEDICAL_KNOWLEDGE:
            tests.extend(MEDICAL_KNOWLEDGE[disease_name]["tests"])
            treatments.extend(MEDICAL_KNOWLEDGE[disease_name]["treatments"])

    # Loại bỏ trùng lặp, vẫn giữ thứ tự ưu tiên theo bệnh có % cao hơn
    tests = list(dict.fromkeys(tests))
    treatments = list(dict.fromkeys(treatments))

    return {
        "diseases": ranked_diseases,
        "no_result_message": None,
        "tests": tests,
        "treatments": treatments
    }
