# -*- coding: utf-8 -*-
from database.score import dict_score_table, dict_std_score_table, dict_converted_score_table, dict_max_score_table


class ScoreDict:
    def __init__(self, dict_test_result, is_original_score=False):
        """
        성적표를 바탕으로 점수 정보를 재구성합니다.
        :param dict_test_result: 성적표 정보
        {
            "한국사": 등급,
            "국어": 표준점수,
            "수학": {
                "수학가형" or "수학나형", 표준점수
            },
            "영어": 등급,
            "탐구": {
                "탐구1": 표준점수,
                "탐구2": 표준점수,
            },
            "제2외국어": {
                "과목명": 표준점수
            }
        }
        """
        self.history = None
        self.korean = None
        self.math = None
        self.english = None
        self.tamgu1 = None
        self.tamgu2 = None
        self.foreign = None
        for key, value in dict_test_result.items():
            if key == "한국사":
                self.history = Score(key, value, is_original_score)
            elif key == "국어":
                self.korean = Score(key, value, is_original_score)
            elif key == "수학":
                # 수학을 응시했다면 무조건 "가" 또는 "나"형 둘 중 하나만의 점수를 가져야 한다.
                if len(value) == 0:
                    pass
                elif len(value) == 1:
                    if "수학가형" in value:
                        self.math = Score("수학가형", value["수학가형"], is_original_score)
                    elif "수학나형" in value:
                        self.math = Score("수학나형", value["수학나형"], is_original_score)
                    else:
                        raise RuntimeError("Invalid math score")
                elif len(value) > 1:
                    raise RuntimeError("Invalid math score")
            elif key == "영어":
                self.english = Score(key, value, is_original_score)
            elif key == "탐구":
                list_tamgu = [Score(tamgu_key, tamgu_value, is_original_score)
                              for tamgu_key, tamgu_value in value.items()]
                if len(list_tamgu) == 0:
                    pass
                elif len(list_tamgu) == 1:
                    tamgu = list_tamgu[0]
                    self.tamgu1 = tamgu
                elif len(list_tamgu) == 2:
                    tamgu1, tamgu2 = list_tamgu[0], list_tamgu[1]
                    if ScoreDict.get_tamgu_class(tamgu1) != ScoreDict.get_tamgu_class(tamgu2):
                        raise RuntimeError("Invalid tamgu score")
                    self.tamgu1 = tamgu1
                    self.tamgu2 = tamgu2
                else:
                    raise RuntimeError("Invalid tamgu score")
            elif key == "제2외국어":
                list_foreign = [Score(foreign_key, foreign_value, is_original_score)
                                for foreign_key, foreign_value in value.items()]
                if len(list_foreign) == 0:
                    pass
                elif len(list_foreign) == 1:
                    foreign = list_foreign[0]
                    self.foreign = foreign
                else:
                    raise RuntimeError("Invalid foreign score")

    def __str__(self):
        return '\n'.join(
            map(str, [self.history, self.korean, self.math, self.english, self.tamgu1, self.tamgu2, self.foreign])
        )

    def __getitem__(self, item):
        try:
            if item == "한국사":
                return self.history
            elif item == "국어":
                return self.korean
            elif item == "수학":
                return self.math
            elif item == "수학가형" or item == "수학나형":
                if self.math and self.math.subject == item:
                    return self.math
                else:
                    return None
            elif item == "영어":
                return self.english
            elif item == "탐구":
                return self.tamgu1, self.tamgu2
            elif item == "사회탐구":
                if self.tamgu1 is None:
                    return None, None
                if ScoreDict.get_tamgu_class(self.tamgu1) == "사회탐구":
                    return self.tamgu1, self.tamgu2
                else:
                    return None, None
            elif item == "과학탐구":
                if self.tamgu1 is None:
                    return None, None
                if ScoreDict.get_tamgu_class(self.tamgu1) == "과학탐구":
                    return self.tamgu1, self.tamgu2
                else:
                    return None, None
            elif item == "제2외국어":
                return self.foreign
        except KeyError:
            return None

    @staticmethod
    def get_tamgu_class(score):
        list_science = [prefix + level for level in ["I", "II"] for prefix in ["물리", "화학", "생명과학", "지구과학"]]
        list_social = ["경제", "동아시아사", "법과정치", "사회·문화", "생활과윤리", "세계지리", "세계사", "윤리와사상", "한국지리"]
        if score.subject in list_science:
            return "과학탐구"
        elif score.subject in list_social:
            return "사회탐구"
        else:
            return None

    @staticmethod
    def is_foreign(score):
        list_foreign = ["독일어I", "러시아어I", "베트남어I", "스페인어I", "아랍어I", "일본어I", "중국어I", "프랑스어I", "한문I"]
        return score.subject in list_foreign


class Score:
    def __init__(self, subject, score, is_orginal_score=False):
        self.original_score = None
        if is_orginal_score:
            self.original_score = score
            score = Score.get_std_score_from_org_score(subject, score)
        self.subject = subject
        if subject == "한국사" or subject == "영어":
            self.grade = score
        else:
            self.score = score
            self.grade = Score.get_grade_from_score(subject, score)
            self.percentage = Score.get_percentage_from_score(subject, score)
            self.upper_accumulation = Score.get_upper_accumulation_from_score(subject, score)
            if subject in dict_max_score_table:
                self.max_score = dict_max_score_table[subject]["표준점수"]
                self.max_percentage = dict_max_score_table[subject]["백분위"]

    def __str__(self):
        if self.subject == "한국사" or self.subject == "영어":
            return f"{self.subject}\n" \
                   f"원점수: {self.original_score}\n" \
                   f"등급: {self.grade}\n"
        else:
            return f"{self.subject}\n" \
                   f"원점수: {self.original_score}\n" \
                   f"표준점수: {self.score}\n" \
                   f"등급: {self.grade}\n" \
                   f"백분위: {self.percentage}\n" \
                   f"상위누적: {self.upper_accumulation}\n"

    def converted_score(self, school):
        if ScoreDict.is_foreign(self):
            score_type = "제2외국어"
        else:
            score_type = ScoreDict.get_tamgu_class(self)
        if score_type is None:
            raise RuntimeError("해당 과목은 탐구 영역 또는 제2외국어·한문에 속하지 않습니다.")
        # 경북대는 제2외국어도 사탐변표 사용
        if score_type == "제2외국어" and school == "경북대":
            score_type = "사회탐구"
        return dict_converted_score_table[score_type][school][100 - self.percentage]

    @staticmethod
    def get_percentage_from_score(subject, std_score):
        return dict_score_table[subject][std_score][0]

    @staticmethod
    def get_grade_from_score(subject, std_score):
        return dict_score_table[subject][std_score][1]

    @staticmethod
    def get_upper_accumulation_from_score(subject, std_score):
        return dict_score_table[subject][std_score][2]

    @staticmethod
    def get_std_score_from_org_score(subject, org_score):
        return dict_std_score_table[subject][org_score]
