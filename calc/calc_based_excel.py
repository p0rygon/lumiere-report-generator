from database.calc_score import dict_calc_score_table, list_calc_key_table
from database.score import dict_converted_score_table


dict_calc_type_table = {'가천식영 이과': ('자유선택', '탐구1과목'), '가천의학 이과': ('가+과 필수', ''), '가천이2 이과': ('가형반영', '탐구1과목,3영역'),
                        '가천이3 이과': ('자유선택', '탐구1과목,3영역'), '가천토목 이과': ('가형필수', '탐구1과목'), '가톨공학 이과': ('자유선택', ''),
                        '가톨의학 이과': ('가+과 필수', ''), '강릉대 이과': ('가+과 필수', ''), '강원공학 이과': ('과탐필수', ''),
                        '강원농생 이과': ('자유선택', '사탐제2대체'), '강원수의 이과': ('가+과 필수', ''), '건국생명 이과': ('가+과 필수', ''),
                        '건국수의 이과': ('가+과 필수', ''), '건국이공 이과': ('가+과 필수', ''), '건양대 이과': ('가+과 필수', ''),
                        '경기자연 이과': ('과탐필수', '탐구1과목'), '경북건축 이과': ('과탐필수', ''), '경북의류 이과': ('자유선택', ''),
                        '경북의학 이과': ('가+과 필수', ''), '경상이공 이과': ('자유선택', ''), '경상의학 이과': ('자유선택', ''),
                        '경인교 이과': ('자유선택', ''), '경희자연 이과': ('가+과 필수', ''), '계명대 이과': ('가+과 필수', ''),
                        '고려가교 이과': ('자유선택', ''), '고려대 이과': ('가+과 필수', ''), '고려사국 이과': ('가+과 필수', ''),
                        '고려경통 이과': ('자유선택', '만점대비'), '': ('', ''), '고려생명 이과': ('과탐 필수', '만점대비'),
                        '고려화학 이과': ('가+과 필수', '만점대비'), '고신대 이과': ('가+과 필수', ''), '공주교 이과': ('자유선택', ''),
                        '공주과교 이과': ('자유선택', '탐구2대체'), '공주수교 이과': ('자유선택', '탐구2대체'), '공주자연 이과': ('자유선택', '탐구2대체'),
                        '과기원 이과': ('가+과 필수', ''), '관동대 이과': ('가+과 필수', ''), '광운건축 이과': ('과탐 필수', ''),
                        '광운이공 이과': ('가+과 필수', ''), '광운정보 이과': ('자유선택', '사탐제2대체'), '광주교 이과': ('자유선택', ''),
                        '교원가교 이과': ('자유선택', ''), '교원과교 이과': ('과탐 필수', ''), '교원수교 이과': ('가+과 필수', ''),
                        '교원초교 이과': ('자유선택', ''), '교원컴교 이과': ('자유선택', ''), '국민대 이과': ('과탐 필수', ''),
                        '단국건축 이과': ('자유선택', ''), '단국의치 이과': ('가+과 필수', ''), '단국이공 이과': ('가+과 필수', ''),
                        '대가대 이과': ('가+과 필수', '탐구1과목'), '대구교 이과': ('자유선택', ''), '대구한 이과': ('가+과 필수', '탐구1과목'),
                        '대전대 이과': ('가+과 필수', ''), '덕성여 이과': ('과탐필수', ''), '동국의학 이과': ('가+과 필수', ''),
                        '동국한의 이과': ('가+과 필수', ''), '동국자연 이과': ('가+과 필수', ''), '동덕여 이과': ('자유선택', ''),
                        '동신대 이과': ('자유선택', '탐구1과목'), '동아대 이과': ('가+과 필수', '생2,화2가산'), '동의대 이과': ('가+과 필수', ''),
                        '명지대 이과': ('자유선택', ''), '부경이공 이과': ('자유선택', ''), '부경자전 이과': ('가+과 필수', ''),
                        '부산교 이과': ('자유선택', ''), '부산생과 이과': ('과탐필수', ''), '부산의학 이과': ('가+과 필수', ''),
                        '삼육대 이과': ('자유선택', '탐구제2대체'), '상명수교 이과': ('가+과 필수', '탐구1과목'), '상명영양 이과': ('자유선택', '탐구1과목'),
                        '상명융합 이과': ('과탐 필수', '탐구1과목'), '상지대 이과': ('자유선택', ''), '서강대 이과': ('자유선택', ''),
                        '서경대 이과': ('자유선택', '탐구제2대체'), '서울과 이과': ('가형 필수', ''), '서울교 이과': ('자유선택', ''),
                        '서울대 이과': ('가+과 필수', ''), '서울여과 이과': ('자유선택', '탐구1과목'), '서울여수 이과': ('자유선택', '탐구1과목'),
                        '서울여패 이과': ('자유선택', '탐구1과목'), '성균관 이과': ('가+과 필수', ''), '성신간이 이과': ('과탐필수', '최상위II가산,탐구제2대체'),
                        '성신통계 이과': ('자유선택', '최상위과탐가산,탐구제2대체'), '성신운동 이과': ('자유선택', '탐구제2대체'),
                        '성신의류 이과': ('자유선택', '탐구제2대체'), '성신수학 이과': ('과탐필수', '탐구제2대체'), '세명대 이과': ('자유선택', ''),
                        '세종대 이과': ('가+과 필수', ''), '세종창의 이과': ('자유선택', ''), '수원간호 이과': ('자유선택', ''),
                        '수원자연 이과': ('자유선택', '탐구1과목'), '숙명물리 이과': ('가+과 필수', ''), '숙명수학 이과': ('가+과 필수', ''),
                        '숙명의류 이과': ('가+과 필수', ''), '숙명이공 이과': ('가+과 필수', ''), '숙명통계 이과': ('가+과 필수', '국/탐선택'),
                        '순천향 이과': ('자유선택', '기본800'), '숭실이공 이과': ('가+과 필수', ''), '숭실정통 이과': ('자유선택', ''),
                        '시립융합 이과': ('가+과 필수', ''), '시립자연 이과': ('가+과 필수', ''), '아주의학 이과': ('가+과 필수', '탐구특이'),
                        '아주자연 이과': ('가+과 필수', '탐구특이'), '연세대 이과': ('가+과 필수', ''), '연원의학 이과': ('가+과 필수', ''),
                        '연원자연 이과': ('가+과 필수', ''), '영남대 이과': ('가+과 필수', ''), '외국어 이과': ('가+과 필수', ''),
                        '우석대 이과': ('자유선택', ''), '울산대 이과': ('가+과 필수', ''), '원광대 이과': ('가+과 필수', ''),
                        '을지대 이과': ('가+과 필수', ''), '이화여 이과': ('가+과 필수', ''), '인제대 이과': ('가+과 필수', ''),
                        '인천자연 이과': ('과탐필수', ''), '인하대 이과': ('가+과 필수', ''), '전남농생 이과': ('자유선택', ''),
                        '전남의학 이과': ('가+과 필수', ''), '전남자전 이과': ('자유선택', ''), '전북간호 이과': ('자유선택', ''),
                        '전북도시 이과': ('과탐필수', ''), '전북의학 이과': ('가+과 필수', ''), '전주교 이과': ('자유선택', ''),
                        '제주수의 이과': ('가+과 필수', ''), '제주의학 이과': ('가+과 필수', ''), '제주초교 이과': ('자유선택', ''),
                        '조선의 이과': ('가+과 필수', ''), '조선치 이과': ('가+과 필수', ''), '중앙대 이과': ('가+과 필수', ''),
                        '진주교 이과': ('자유선택', ''), '청주교 이과': ('자유선택', ''), '춘천교 이과': ('자유선택', ''), '충남농생 이과': ('자유선택', ''),
                        '충남의학 이과': ('가+과 필수', ''), '충남이공 이과': ('과탐필수', ''), '충북사범 이과': ('과탐필수', '기본740'),
                        '충북생활 이과': ('자유선택', '기본790'), '충북수의 이과': ('가+과 필수', '기본800'), '충북의학 이과': ('가+과 필수', '기본750'),
                        '충북이공 이과': ('과탐필수', '기본790'), '충북자전 이과': ('자유선택', '기본790'), '한경자원 이과': ('자유선택', '탐구1과목'),
                        '한경컴공 이과': ('자유선택', '탐구1과목'), '한림대 이과': ('가+과 필수', ''), '한성대 이과': ('자유선택', '국수상위가중'),
                        '한양가 이과': ('가+과 필수', ''), '한양나 이과': ('가+과 필수', ''), '한양에자 이과': ('가+과 필수', ''),
                        '항공공학 이과': ('가+과 필수', ''), '항공소프 이과': ('자유선택', ''), '항공운항 이과': ('자유선택', ''),
                        '해양경찰 이과': ('자유선택', ''), '해양공학 이과': ('자유선택', ''), '해양해사 이과': ('자유선택', ''),
                        '홍익대 이과': ('가+과 필수', ''), '가천의학 문과': ('자유선택', ''), '가천문2 문과': ('자유선택', '탐구1과목,3영역'),
                        '가천인문 문과': ('자유선택', '탐구1과목'), '가톨간문 문과': ('나+사 필수', '탐구제2대체'), '가톨인문 문과': ('자유선택', '탐구제2대체'),
                        '강원간호 문과': ('사탐필수', '사탐제2대체'), '강원인문 문과': ('자유선택', '사탐제2대체'), '건국상경 문과': ('나형 필수', '탐구제2대체'),
                        '건국인문 문과': ('나형 필수', '탐구제2대체'), '경기국제 문과': ('자유선택', '국/수선택,탐구1과목'),
                        '경기법경 문과': ('자유선택', '탐구1과목'), '경기유교 문과': ('자유선택', '탐구1과목'), '경기인문 문과': ('자유선택', '탐구1과목'),
                        '경북독교 문과': ('자유선택', '탐구독어대체'), '경북불교 문과': ('자유선택', '탐구불어대체'), '경북사회 문과': ('자유선택', ''),
                        '경북인문 문과': ('자유선택', '탐구제2대체'), '경상인문 문과': ('자유선택', ''), '경인교 문과': ('자유선택', ''),
                        '경희사회 문과': ('나+사 필수', '사탐제2대체'), '경희인문 문과': ('나+사 필수', '사탐제2대체'), '고려가교 문과': ('자유선택', ''),
                        '고려간호 문과': ('가+과 불가', ''), '고려대 문과': ('자유선택', ''), '고려경통 문과': ('자유선택', '만점대비'),
                        '고려글로 문과': ('자유선택', '만점대비,수/탐선택'), '공주교 문과': ('자유선택', ''), '공주교육 문과': ('자유선택', '탐구제2대체'),
                        '공주인문 문과': ('자유선택', '탐구제2대체'), '관동대 문과': ('자유선택', ''), '광운상경 문과': ('자유선택', '사탐제2대체'),
                        '광운인문 문과': ('자유선택', '사탐제2대체'), '광주교 문과': ('자유선택', ''), '교원국교 문과': ('자유선택', ''),
                        '교원영교 문과': ('자유선택', ''), '교원외교 문과': ('자유선택', '탐구제2대체'), '교원유교 문과': ('자유선택', ''),
                        '교원초교 문과': ('자유선택', ''), '국민대 문과': ('자유선택', ''), '단국상경 문과': ('나형 필수', ''),
                        '단국인문 문과': ('나형 필수', '탐구제2대체'), '대구교 문과': ('자유선택', ''), '대구한 문과': ('나+사 필수', '탐구1과목'),
                        '대전대 문과': ('나+사 필수', ''), '덕성여 문과': ('자유선택', ''), '동국인문 문과': ('자유선택', '탐구제2대체'),
                        '동국한의 문과': ('사탐필수', ''), '동덕여 문과': ('자유선택', ''), '동신대 문과': ('자유선택', '탐구1과목'),
                        '동의대 문과': ('나+사 필수', ''), '명지대 문과': ('자유선택', ''), '부경인문 문과': ('자유선택', ''),
                        '부경자전 문과': ('나+사 필수', ''), '부산교 문과': ('자유선택', ''), '부산노문 문과': ('자유선택', '제2가산'),
                        '부산독문 문과': ('자유선택', '제2가산'), '부산불문 문과': ('자유선택', '제2가산'), '부산사회 문과': ('자유선택', ''),
                        '부산일문 문과': ('자유선택', '제2가산'), '부산중문 문과': ('자유선택', '제2가산'), '부산한문 문과': ('자유선택', '제2가산'),
                        '삼육대 문과': ('자유선택', '탐구제2대체'), '상명인문 문과': ('자유선택', '탐구1과목'), '상지대 문과': ('자유선택', ''),
                        '서강대 문과': ('자유선택', ''), '서경대 문과': ('자유선택', '탐구제2대체'), '서울간호 문과': ('가+과 불가', ''),
                        '서울과 문과': ('나형 필수', ''), '서울교 문과': ('자유선택', ''), '서울대 문과': ('자유선택', '제2감점'),
                        '서울여문 문과': ('자유선택', '탐구1과목'), '서울의류 문과': ('가+과 불가', '제2감점'), '성균관 문과': ('자유선택', '탐구제2대체'),
                        '성신간문 문과': ('사탐필수', '가형가산,탐구제2대체'), '성신글로 문과': ('자유선택', '탐구제2대체,3영역'),
                        '성신상경 문과': ('자유선택', '탐구제2대체'), '성신인문 문과': ('자유선택', '탐구제2대체'), '세명대 문과': ('자유선택', ''),
                        '세종대 문과': ('나+사 필수', ''), '수원문화 문과': ('자유선택', '탐구1과목'), '수원인문 문과': ('자유선택', '탐구1과목'),
                        '숙명경상 문과': ('자유선택', '사탐제2대체'), '숙명소프 문과': ('나형 필수', ''), '숙명의류 문과': ('나형 필수', '사탐제2대체'),
                        '숙명인문 문과': ('자유선택', '사탐제2대체'), '숙명통계 문과': ('나형 필수', '국/탐선택'), '숭실상경 문과': ('자유선택', '사탐제2대체'),
                        '숭실인문 문과': ('자유선택', '사탐제2대체'), '시립상경 문과': ('자유선택', '탐구제2대체'), '시립인문 문과': ('자유선택', '탐구제2대체'),
                        '시립자전 문과': ('자유선택', '탐구제2대체'), '아주경영 문과': ('나+사 필수', '탐구특이'), '아주인문 문과': ('나+사 필수', '탐구특이'),
                        '연세대 문과': ('자유선택', '탐구제2대체'), '연원사회 문과': ('자유선택', '탐구제2대체'), '연원인문 문과': ('자유선택', '탐구제2대체'),
                        '외국어 문과': ('자유선택', '사탐제2대체'), '우석대 문과': ('자유선택', ''), '원광대 문과': ('나+사 필수', ''),
                        '이화여 문과': ('나형 필수', '탐구제2대체'), '인천동북 문과': ('자유선택', '탐구제2대체'), '인천인문 문과': ('자유선택', ''),
                        '인하아태 문과': ('나+사 필수', '사탐제2대체'), '인하인문 문과': ('나+사 필수', '사탐제2대체'), '전남사회 문과': ('자유선택', ''),
                        '전남인문 문과': ('자유선택', '사탐제2대체'), '전북상경 문과': ('자유선택', ''), '전북인문 문과': ('나+사 필수', ''),
                        '전북독교 문과': ('자유선택', '사탐독어대체'), '전북독어 문과': ('나+사 필수', '사탐독어대체'), '전북불어 문과': ('나+사 필수', '사탐불어대체'),
                        '전북서어 문과': ('나+사 필수', '사탐서어대체'), '전북일어 문과': ('자유선택', '사탐일어대체'), '전북중어 문과': ('자유선택', '사탐중어대체'),
                        '전주교 문과': ('자유선택', ''), '제주초교 문과': ('자유선택', ''), '중앙대 문과': ('자유선택', '사탐제2대체'),
                        '진주교 문과': ('자유선택', ''), '청주교 문과': ('자유선택', ''), '춘천교 문과': ('자유선택', ''), '충남사회 문과': ('자유선택', ''),
                        '충남어문 문과': ('자유선택', '제2가산'), '충북사범 문과': ('자유선택', '기본750'), '충북인문 문과': ('자유선택', '기본800'),
                        '충북자전 문과': ('자유선택', '기본790'), '한성대 문과': ('자유선택', '국수상위가중'), '한경인문 문과': ('자유선택', '탐구1과목'),
                        '한양가상 문과': ('나+사 필수', '사탐제2대체'), '한양가인 문과': ('나+사 필수', '사탐제2대체'),
                        '한양나상 문과': ('나+사 필수', '사탐제2대체'), '한양나인 문과': ('나+사 필수', '사탐제2대체'),
                        '한양에문 문과': ('나+사 필수', '사탐제2대체'), '한양에보 문과': ('나+사 필수', '사탐제2대체'), '항공경영 문과': ('자유선택', ''),
                        '해양인문 문과': ('자유선택', ''), '홍익대 문과': ('자유선택', '')}


def acc_round(x, n):
    return round(x + 1e-15, n)  # It solve floating point error like round(1.5, 1) = 1


class Calculator:
    def __init__(self, calc_key, score_dict):
        self.calc_key = calc_key
        self.score_dict = score_dict

    def calc(self):
        score_dict = self.score_dict
        calc_idx = list_calc_key_table.index(self.calc_key)

        history = score_dict["한국사"]
        korean = score_dict["국어"]
        math = score_dict["수학"]
        english = score_dict["영어"]
        tamgu1, tamgu2 = score_dict["탐구"]
        foreign = score_dict["제2외국어"]

        # 한국사 미응시시 성적 미산출
        if not history:
            return 0.0

        select_type, calc_type = dict_calc_type_table[self.calc_key]
        # 필수선택 확인
        if select_type == "가+과 필수":
            if not (score_dict["수학가형"] and score_dict["과학탐구"][0]):
                return 0.0
        elif select_type == "가형필수" or select_type == "가형 필수":
            if not (score_dict["수학가형"]):
                return 0.0
        elif select_type == "과탐필수" or select_type == "과탐 필수":
            if not (score_dict["과학탐구"][0]):
                return 0.0
        elif select_type == "사탐필수" or select_type == "사탐 필수":
            if not (score_dict["사회탐구"][0]):
                return 0.0
        elif select_type == "나형필수" or select_type == "나형 필수":
            if not (score_dict["수학나형"]):
                return 0.0
        if select_type == "나+사 필수":
            if not (score_dict["수학나형"] and score_dict["사회탐구"][0]):
                return 0.0
        elif select_type == "가+과 불가":
            if score_dict["수학가형"] and score_dict["과학탐구"][0]:
                return 0.0

        # 과목별 점수 초기화
        score_history = 0.0
        score_korean = 0.0
        score_math = 0.0
        score_english = 0.0
        score_tamgu1 = 0.0
        score_tamgu2 = 0.0
        score_foreign = 0.0
        if history:
            score_history = float(dict_calc_score_table[history.subject][history.grade][calc_idx])
        if english:
            score_english = float(dict_calc_score_table[english.subject][english.grade][calc_idx])
        if korean:
            score_korean = float(dict_calc_score_table[korean.subject][korean.score][calc_idx])
        if math:
            score_math = float(dict_calc_score_table[math.subject][math.score][calc_idx])
        if tamgu1:
            score_tamgu1 = float(dict_calc_score_table[tamgu1.subject][tamgu1.score][calc_idx])
        if tamgu2:
            score_tamgu2 = float(dict_calc_score_table[tamgu2.subject][tamgu2.score][calc_idx])
        if foreign:
            score_foreign = float(dict_calc_score_table[foreign.subject][foreign.score][calc_idx])


        score = 0.0
        # 이상한 학교들
        if self.calc_key.startswith("충북"):
            # 기본 XXX (기본점수 XXX점 제공)
            if tamgu1 and tamgu2:
                score_tamgu = (tamgu1.score + tamgu2.score) / (tamgu1.max_score + tamgu2.max_score) * 60
                for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu, score_foreign]:
                    score += score_subject
            else:
                return 0.0
        elif self.calc_key.startswith("순천향"):
            # 기본 800점이라 충북이랑 같이 묶음
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu1, score_tamgu2, score_foreign]:
                score += score_subject

        # 계산방식에 따라 계산
        if calc_type == "":
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu1, score_tamgu2, score_foreign]:
                score += score_subject
        elif calc_type == "탐구1과목":
            score_tamgu = max(score_tamgu1, score_tamgu2)
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu, score_foreign]:
                score += score_subject
        elif calc_type == "탐구1과목,3영역":
            score_tamgu = max(score_tamgu1, score_tamgu2)
            list_score = sorted([score_history, score_english, score_korean, score_math, score_tamgu, score_foreign], reverse=True)
            score += list_score[0] * 4 + list_score[1] * 4 + list_score[2] * 2
        elif calc_type == "사탐제2대체":
            if score_dict["사회탐구"][0]:
                score_tamgu = score_tamgu1 + score_tamgu2 + score_foreign - min(score_tamgu1, score_tamgu2, score_foreign)
            else:
                score_tamgu = score_tamgu1 + score_tamgu2
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu]:
                score += score_subject
        elif calc_type == "만점대비":
            # 고대세종
            if not (korean and math and english and tamgu1 and tamgu2):
                return 0.0
            score_max = float(dict_calc_score_table[english.subject][1][calc_idx])
            score_max += float(dict_calc_score_table[korean.subject][korean.max_score][calc_idx])
            if self.calc_key == "고려화학 이과" or self.calc_key.startswith("고려경통"):
                score_max += float(dict_calc_score_table[math.subject][math.max_score][calc_idx])
            else:
                score_max += float(dict_calc_score_table[math.subject][math.max_score][calc_idx]) / 1.10
            if score_dict["과학탐구"][0]:
                score_tamgu_max = dict_converted_score_table["과학탐구"]["고려세"][0] * 2
            elif score_dict["사회탐구"][0]:
                score_tamgu_max = dict_converted_score_table["사회탐구"]["고려세"][0] * 2
            if self.calc_key.endswith("이과"):
                score_max += score_tamgu_max * 0.167
            elif self.calc_key == "고려경통 문과":
                score_max += score_tamgu_max * 0.142

            score = score_english
            for score_subject in [score_korean, score_math, score_tamgu1, score_tamgu2]:
                score += score_subject
            score = score / score_max * 1000
        elif calc_type == "만점대비,수/탐선택":
            # 고대세종 -  고려글로 문과
            if not (korean and math and english and tamgu1 and tamgu2):
                return 0.0
            score_max = float(dict_calc_score_table[english.subject][1][calc_idx])
            score_max += float(dict_calc_score_table[korean.subject][korean.max_score][calc_idx])
            score_max += float(dict_calc_score_table[math.subject][math.max_score][calc_idx])

            score = score_english
            for score_subject in [score_korean, score_math]:
                score += score_subject
            score = score / score_max * 1000
            score_with_math = score

            score_max = float(dict_calc_score_table[english.subject][1][calc_idx])
            score_max += float(dict_calc_score_table[korean.subject][korean.max_score][calc_idx])
            if score_dict["과학탐구"][0]:
                score_tamgu_max = dict_converted_score_table["과학탐구"]["고려세"][0] * 2
            elif score_dict["사회탐구"][0]:
                score_tamgu_max = dict_converted_score_table["사회탐구"]["고려세"][0] * 2
            score_max += score_tamgu_max * 0.2

            score = score_english
            for score_subject in [score_korean, score_tamgu1, score_tamgu2]:
                score += score_subject
            score = score / score_max * 1000
            score_with_tamgu = score

            score = max(score_with_math, score_with_tamgu)
        elif calc_type == "탐구제2대체" or calc_type == "탐구2대체":
            score_tamgu = score_tamgu1 + score_tamgu2 + score_foreign - min(score_tamgu1, score_tamgu2, score_foreign)
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu]:
                score += score_subject
        elif calc_type == "생2,화2가산":
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu1, score_tamgu2, score_foreign]:
                score += score_subject
            if tamgu1 and tamgu2:
                list_tamgu = [tamgu1.subject, tamgu2.subject]
                if "생명과학II" in list_tamgu and "화학II" in list_tamgu:
                    score -= 3.0
        elif calc_type == "최상위II가산,탐구제2대체":
            # 성신여대
            if tamgu1 and tamgu2:
                if tamgu1.percentage > tamgu2.percentage:
                    if tamgu1.subject in ["물리II", "화학II", "생명과학II"]:
                        score += tamgu1.percentage * 0.05
                    else:
                        if tamgu2.subject in ["물리II", "화학II", "생명과학II"]:
                            score += tamgu2.percentage * 0.05
                else:
                    if tamgu2.subject in ["물리II", "화학II", "생명과학II"]:
                        score += tamgu2.percentage * 0.05
                    else:
                        if tamgu1.subject in ["물리II", "화학II", "생명과학II"]:
                            score += tamgu1.percentage * 0.05
            elif tamgu1:
                if tamgu1.subject in ["물리II", "화학II", "생명과학II"]:
                    score += tamgu1.percentage * 0.05
            score_tamgu = score_tamgu1 + score_tamgu2 + score_foreign - min(score_tamgu1, score_tamgu2, score_foreign)
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu]:
                score += score_subject
        elif calc_type == "최상위과탐가산,탐구제2대체":
            # 성신여대
            if score_dict["과학탐구"][0]:
                if tamgu1.percentage and tamgu2.percentage:
                    if score_tamgu1 > score_tamgu2:
                        score += tamgu1.percentage * 0.1
                    else:
                        score += tamgu2.percentage * 0.1
                elif tamgu1:
                    score += tamgu1.percentage * 0.1
            score_tamgu = score_tamgu1 + score_tamgu2 + score_foreign - min(score_tamgu1, score_tamgu2, score_foreign)
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu]:
                score += score_subject
        elif calc_type == "국/탐선택":
            score_tamgu = score_tamgu1 + score_tamgu2
            if score_korean > score_tamgu:
                score_korean_tamgu = score_korean
            else:
                score_korean_tamgu = score_tamgu
            for score_subject in [score_history, score_english, score_korean_tamgu, score_math]:
                score += score_subject
        elif calc_type.startswith("기본"):
            base_score = int(calc_type.replace("기본", ""))
            score += base_score
        elif calc_type == "탐구특이":
            # 아주대
            dict_multiply_const = {
                "아주의학 이과": 280, "아주자연 이과": 250, "아주경영 문과": 150, "아주인문 문과": 200
            }
            if tamgu1 and tamgu2:
                score_max = float(dict_calc_score_table[tamgu1.subject][tamgu1.max_score][calc_idx]) \
                            + float(dict_calc_score_table[tamgu2.subject][tamgu2.max_score][calc_idx])
                score_tamgu = (score_tamgu1 + score_tamgu2) / score_max * dict_multiply_const[self.calc_key]
                for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu, score_foreign]:
                    score += score_subject
        elif calc_type == "국수상위가중":
            if score_korean > score_math:
                score += score_korean * 4
                score += score_math * 2
            else:
                score += score_math * 4
                score += score_korean * 2
            for score_subject in [score_history, score_english, score_tamgu1, score_tamgu2, score_foreign]:
                score += score_subject
        elif calc_type == "국/수선택,탐구1과목":
            if score_korean > score_math:
                score += score_korean
            else:
                score += score_math
            score_tamgu = max(score_tamgu1, score_tamgu2)
            for score_subject in [score_history, score_english, score_tamgu, score_foreign]:
                score += score_subject
        elif calc_type == "탐구독어대체":
            if foreign and foreign.subject == "독일어I":
                score_tamgu = score_tamgu1 + score_tamgu2 + score_foreign - min(score_tamgu1, score_tamgu2, score_foreign)
            else:
                score_tamgu = score_tamgu1 + score_tamgu2
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu]:
                score += score_subject
        elif calc_type == "탐구불어대체":
            if foreign and foreign.subject == "프랑스어I":
                score_tamgu = score_tamgu1 + score_tamgu2 + score_foreign - min(score_tamgu1, score_tamgu2, score_foreign)
            else:
                score_tamgu = score_tamgu1 + score_tamgu2
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu]:
                score += score_subject
        elif calc_type == "제2가산":
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu1, score_tamgu2, score_foreign]:
                score += score_subject
        elif calc_type == "제2감점":
            if not (score_dict["수학가형"] or score_dict["제2외국어"]):
                score_foreign -= 3.5
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu1, score_tamgu2, score_foreign]:
                score += score_subject
        elif calc_type == "가형가산,탐구제2대체":
            # 성신여대
            if not math:
                return 0.0
            if score_dict["수학가형"]:
                score += math.percentage * 0.1
            score_tamgu = score_tamgu1 + score_tamgu2 + score_foreign - min(score_tamgu1, score_tamgu2, score_foreign)
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu]:
                score += score_subject
        elif calc_type == "탐구제2대체,3영역":
            score_tamgu = score_tamgu1 + score_tamgu2 + score_foreign - min(score_tamgu1, score_tamgu2, score_foreign)
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu]:
                score += score_subject
            score -= min(score_korean, score_math, score_english, score_tamgu)
        elif calc_type.startswith("사탐") and calc_type.endswith("어대체"):
            dict_target_foreign = {
                "독": "독일어I", "불": "프랑스어I", "서": "러시아어I", "일": "일본어I", "중": "중국어I"
            }
            target_foreign = dict_target_foreign[calc_type[2]]
            if score_dict["사회탐구"] and score_dict["제2외국어"]:
                if foreign.subject == target_foreign:
                    score_tamgu = score_tamgu1 + score_tamgu2 + score_foreign - min(score_tamgu1, score_tamgu2, score_foreign)
                else:
                    score_tamgu = score_tamgu1 + score_tamgu2
            else:
                score_tamgu = score_tamgu1 + score_tamgu2
            for score_subject in [score_history, score_english, score_korean, score_math, score_tamgu]:
                score += score_subject

        return acc_round(score, 3)
