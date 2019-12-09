# -*- coding: utf-8 -*-
import pdfkit
from time import localtime, strftime

from database.unit import dict_school_name_table, dict_school_calc_table, dict_unit_table
from database.nb import dict_nb_table
# from .calc import dict_calculator
from calc.calc_based_excel import Calculator
from score import ScoreDict
import config


NUMBER_OF_MAJOR_IN_PAGE = 10
BAR_SIZE_UNION = 1020


def acc_round(x, n):
    return round(x + 1e-15, n)  # It solve floating point error like round(1.5, 1) = 1


def ceil(f):
    return int(f) + (1 if f - int(f) else 0)


def read_html(filename):
    file = open('./docs/' + filename + '.htm', encoding='utf-8')
    return file.read()


def convert_html_to_pdf(infile, outfile):
    options = {
        'page-size': 'A4',
        'zoom': 96 / 230,
        'disable-smart-shrinking': '',
        'margin-top': '0px',
        'margin-right': '0px',
        'margin-bottom': '0px',
        'margin-left': '0px',
        'encoding': "UTF-8",
        'orientation': 'Landscape',
        'title': 'Lumiere 2020'
    }
    config = pdfkit.configuration(wkhtmltopdf="./wkhtmltopdf")
    pdfkit.from_file(infile, outfile, options=options, configuration=config)


def get_nb(calc_key, score):
    if score == "-":
        return 0.0
    if score == 0.0:
        return 100.0
    nb_table = dict_nb_table[calc_key]
    list_nb = nb_table["list_nb"]
    if score > nb_table["max_score"]:
        return 0.0
    elif score < nb_table["min_score"]:
        return "> " + str(acc_round(list_nb[-1], 1))
    else:
        nb = list_nb[int(acc_round((nb_table["max_score"] - score) / 0.1, 0))]
        if nb < 1.0:
            return acc_round(nb, 3)
        elif 1.0 <= nb < 10.0:
            return acc_round(nb, 2)
        else:
            return acc_round(nb, 1)


def get_nb_list(calc_key, converted_score, affiliation):
    # 모집단위 관련 변수 예시
    # (PARAMETER) school: 서울대 이과, affiliation: 이과 / 문과
    # (INTERNAL VARIABLE) school_name: 서울대, aff_type: 이과

    people_count = config.people_count[affiliation]   # 수학 가형 응시인원 수
    list_score = list()
    list_rank = list()
    list_nb = list()
    max_score = dict_nb_table[calc_key]["max_score"]
    min_score = dict_nb_table[calc_key]["min_score"]
    nb_table = dict_nb_table[calc_key]["list_nb"]
    if converted_score < min_score:  # 점수가 너무 낮아서 리스트에 없음
        # 맨 뒤의 5개 리스트에 넣기
        for i in range(5):
            list_score.append(
                acc_round(min_score + (i - 5) * 0.5, 1)
            )
        list_rank += list(map(
                lambda x: str(format(int(0.01 * x * people_count), ',d')),
                nb_table[-25:][::5]
            ))
        list_nb += list(map(lambda x:str(x) + '%', acc_round(nb_table[-25:][::5], 3)))
        # 유저 성적 넣기
        list_score.append(converted_score)
        list_rank.append('> ' + format(int(0.01 * nb_table[-1] * people_count), ',d'))
        list_nb.append('> ' + str(acc_round(nb_table[-1], 3)) + '%')
        # 빈칸으로 채우기
        for i in range(5):
            list_score.append('')
            list_rank.append('')
            list_nb.append('')
    elif max_score < converted_score:     # 리스트상 최고점보다 높은 점수
        # 빈칸으로 채우기
        for i in range(5):
            list_score.append('')
            list_rank.append('')
            list_nb.append('')
        # 유저 정보 넣기
        list_score.append(converted_score)
        list_rank.append('< ' + format(int(0.01 * nb_table[0] * people_count), ',d'))
        list_nb.append('< ' + str(acc_round(nb_table[0], 3)) + '%')
        # 맨 앞의 5개 리스트에 넣기
        for i in range(5):
            list_score.append(acc_round(max_score - 0.5 * i, 1))
        list_rank += list(map(lambda x: format(int(0.01 * x * people_count), ',d'), acc_round(nb_table[0:25:5], 3)))
        list_nb += list(map(lambda x:str(x) + '%', acc_round(nb_table[0:25:5], 3)))
    else:
        for i in range(-5, 6):
            if i == 0:
                now_idx_score = converted_score
            else:
                now_idx_score = acc_round(converted_score - i * 0.5, 1)
            # 학교별 누백 표에 있는 점수면 넣고
            if min_score <= now_idx_score <= max_score:
                list_score.append(now_idx_score)
                table_idx = int(acc_round((max_score - now_idx_score) / 0.1, 0))
                list_rank.append(
                    format(int(0.01 * nb_table[table_idx] * people_count), ',d')
                )
                list_nb.append(str(acc_round(nb_table[table_idx], 3)) + '%')
            else: # 학교별 누백 표에 없는 점수면 빈칸으로 채운다
                list_score.append('')
                list_rank.append('')
                list_nb.append('')
        list_score[5] = converted_score

    return list(map(str, list_score)), list_rank, list_nb


def generate_report(list_school, affiliation, dict_test, is_original_score=False):
    # load templates
    template = read_html("templates")
    nb_page = read_html("nb_page")  # string
    nb_tr = read_html("nb_tr")  # string
    union_nb_page = read_html("union_nb_page")  # string
    union_nb_tr = read_html("union_nb_tr")  # string
    p_page = read_html("union_p_page")    # string
    p_tr = read_html("union_p_tr")        # string
    custom_section = ""
    people_count = config.people_count[affiliation]

    def get_rank(nb):
        if isinstance(nb, float):
            rank = str(format(int(0.01 * nb * people_count), ",d"))
        else:
            float_nb = float(nb[2:])
            rank = nb[:2] + str(format(int(0.01 * float_nb * people_count), ",d"))
        return rank

    score_dict = ScoreDict(dict_test, is_original_score)
    ############### 성적 분석 페이지 생성
    # 선택과목에 따른 성적 분석 표 header 변경
    korean = score_dict["국어"]

    math = score_dict["수학"]
    if math:
        if math.subject == "수학가형":
            math_type = "가"
        else:
            math_type = "나"
    else:
        math_type = "-"
    template = template.replace("math_kind", math_type)

    english = score_dict["영어"]
    history = score_dict["한국사"]

    tamgu1, tamgu2 = score_dict["탐구"]
    if tamgu1:
        tamgu_type = score_dict.get_tamgu_class(tamgu1)
    else:
        tamgu_type = "-"
    template = template.replace("tamgu_kind", tamgu_type)
    template = template.replace("sub_1", tamgu1.subject if tamgu1 else "-")
    template = template.replace("sub_2", tamgu2.subject if tamgu2 else "-")

    foreign = score_dict["제2외국어"]
    if foreign:  # 제2외국어 선택시
        template = template.replace("sub_3", foreign.subject)
    else:  # 제2외국어 미선택시
        template = template.replace("sub_3", "-")

    # 점수 기입
    sum_zscore = 0
    sum_percentage = 0
    for subject_idx, subject in enumerate([korean, math, english, history, tamgu1, tamgu2, foreign]):
        if subject:
            if subject.subject == "한국사" or subject.subject == "영어":
                list_score = [
                    subject.original_score,
                    "",
                    "",
                    subject.grade,
                    "",
                ]
            else:
                list_score = [
                    subject.original_score,
                    subject.score,
                    subject.percentage,
                    subject.grade,
                    str(subject.upper_accumulation) + "%",
                ]
                if subject_idx in [0, 1]:
                    sum_zscore += subject.score
                    sum_percentage += subject.percentage
                elif subject_idx in [4, 5]:
                    sum_zscore += subject.score
                    sum_percentage += subject.percentage / 2
            for score_idx, score in enumerate(list_score):
                template = template.replace(f"{subject_idx + 1}s_{score_idx}", str(score))
        else:
            for score_idx in range(5):
                template = template.replace(f"{subject_idx + 1}s_{score_idx}", "-")

    # 표준점수 합
    zscore_nb = get_nb(f"★표점합 {affiliation}", sum_zscore)
    zscore_rank = get_rank(zscore_nb)
    template = template.replace("sum_zscore", str(sum_zscore)) \
                       .replace("zscore-rank", str(zscore_rank)) \
                       .replace("zscore-nb", str(zscore_nb))

    # 백분위 합
    percentage_nb = get_nb(f"★백분위합 {affiliation}", sum_percentage)
    percentage_rank = get_rank(percentage_nb)
    template = template.replace("sum_percentage", str(sum_percentage)) \
                       .replace("percentage-rank", str(percentage_rank)) \
                       .replace("percentage-nb", str(percentage_nb))

    # 누백 기준, 응시 인원
    template = template.replace("rank_type", "수학 가형" if affiliation == "이과" else "수학 나형") \
                       .replace("people_count", str(format(people_count, ",d") + "명"))

    ############### 학교별 데이터 생성
    for school in list_school:
        # check school type
        #print(school, affiliation, list(dict_school_calc_table[school].keys()))
        if affiliation not in dict_school_calc_table[school]:
            continue
        is_school_type_union = len(dict_school_calc_table[school][affiliation]) != 1

        ############### 계산식 별 점수, 누백 계산
        dict_converted_score = dict()
        for calc_key in dict_school_calc_table[school][affiliation]:
            calc_key = calc_key + " " + affiliation
            # calc = dict_calculator[calc_key](score_dict)
            calc = Calculator(calc_key, score_dict)
            converted_score = calc.calc()
            converted_nb = get_nb(calc_key, converted_score)
            dict_converted_score[calc_key] = {"score": converted_score, "nb": converted_nb}

        ############### 누백 table 생성
        if is_school_type_union:
            now_nb_page = union_nb_page
            # 누백 표
            now_nb_tr = ""
            for_now_nb_tr = union_nb_tr
            for unit_idx, (unit, unit_data) in enumerate(dict_unit_table[school][affiliation].items()):
                # unit: 모집단위 약어
                # unit_data: 계산식, 모집단위, 모집군, 모집정원, 안정컷, 예상컷, 소신컷
                calc_key = unit_data[0] + ' ' + affiliation
                converted_score = dict_converted_score[calc_key]["score"]
                converted_nb = dict_converted_score[calc_key]["nb"]
                converted_rank = get_rank(converted_nb)
                for_now_nb_tr = for_now_nb_tr.replace(f"nn0{unit_idx % 3 + 1}", unit) \
                    .replace(f"ns0{unit_idx % 3 + 1}", str(converted_score)) \
                    .replace(f"nr0{unit_idx % 3 + 1}", converted_rank) \
                    .replace(f"nb0{unit_idx % 3 + 1}", str(converted_nb) + "%")
                if (unit_idx + 1) % 3 == 0:
                    now_nb_tr += for_now_nb_tr
                    for_now_nb_tr = union_nb_tr
            if len(dict_unit_table[school][affiliation]) % 3 != 0:
                if "nn02" in for_now_nb_tr:
                    for_now_nb_tr = for_now_nb_tr.replace("nn02", "") \
                        .replace("ns02", "") \
                        .replace("nr02", "") \
                        .replace("nb02", "")
                if "nn03" in for_now_nb_tr:
                    for_now_nb_tr = for_now_nb_tr.replace("nn03", "") \
                        .replace("ns03", "") \
                        .replace("nr03", "") \
                        .replace("nb03", "")
                now_nb_tr += for_now_nb_tr
                for_now_nb_tr = union_nb_tr
            now_nb_page = now_nb_page.replace(union_nb_tr, now_nb_tr) \
                                     .replace("school_name", dict_school_name_table[school])
        else:
            calc_key = dict_school_calc_table[school][affiliation][0] + " " + affiliation
            converted_score = dict_converted_score[calc_key]["score"]
            now_nb_page = nb_page
            # 총 변환점수
            now_nb_page = now_nb_page.replace('converted_score', str(converted_score))
            # 누백 표
            now_nb_tr = nb_tr
            for i in range(2, 12):
                now_nb_tr += nb_tr.replace('01', str(i).zfill(2))
            nblist = get_nb_list(calc_key, converted_score, affiliation)
            for i in range(11):
                now_nb_tr = now_nb_tr.replace('ns' + str(i + 1).zfill(2), nblist[0][i])
                now_nb_tr = now_nb_tr.replace('nr' + str(i + 1).zfill(2), nblist[1][i])
                now_nb_tr = now_nb_tr.replace('nb' + str(i + 1).zfill(2), nblist[2][i])
            now_nb_page = now_nb_page.replace(nb_tr, now_nb_tr) \
                                     .replace("school_name", dict_school_name_table[school])

        ############### 합격 예상 table 생성
        now_page = ""
        now_table = ""
        for unit_idx, (unit, unit_data) in enumerate(dict_unit_table[school][affiliation].items()):
            # unit_data: 계산식, 모집단위, 모집군, 모집정원, 안정컷, 예상컷, 소신컷
            calc_key = unit_data[0] + ' ' + affiliation
            converted_score = dict_converted_score[calc_key]["score"]
            converted_nb = dict_converted_score[calc_key]["nb"]

            list_cut = list(unit_data[4:])
            if list_cut[2] == '-':
                list_cut = ['-'] * 5
                list_cut_nb = ['-'] * 5
                list_bar_size = [25] * 5
                list_cut_pos = [0, 23, 48, 73, 0]
                now_p_tr = p_tr
                score_pos = 1.0
                score_cursor_pos = 99.5
                score_pos = 100 - (score_pos * BAR_SIZE_UNION + 10) / BAR_SIZE_UNION * 100
                score_cursor = f"<p class=\"p_pos_score\" style=\"right: {score_pos}%;\">" \
                               f"{converted_score}({converted_nb}%) <span class=\"p_pos\"></span></p>"
                signal_type = "red"  # 빨강
            else:
                if converted_score < list_cut[2]:
                    signal_type = "red"          # 빨강
                elif list_cut[2] <= converted_score < list_cut[1]:
                    signal_type = "yellow"             # 노랑
                elif list_cut[1] <= converted_score < list_cut[0]:
                    signal_type = "light_green"     # 연초록
                else:
                    signal_type = "green"           # 진초록
                delta = (list_cut[0] - list_cut[2]) * 0.4
                start = acc_round(list_cut[2] - delta, 3)
                end = acc_round(list_cut[0] + delta, 3)
                list_cut = [end] + list_cut + [start]
                list_cut_nb = [get_nb(calc_key, cut) for cut in list_cut]

                list_bar_size = [(list_cut[i-1] - list_cut[i]) / (end - start) * 100 for i in [1, 2, 3, 4]]
                list_bar_size.append(100 - sum(list_bar_size))
                list_cut_pos = [0, 22, 45 + (sum(list_bar_size[:2]) - 51) * 0.25, 66, 0]
                now_p_tr = p_tr
                score_pos = (end - converted_score) / (end - start)
                score_cursor_pos = (score_pos * BAR_SIZE_UNION - 2) / BAR_SIZE_UNION * 100
                if score_cursor_pos < 0.0:
                    score_cursor_pos = 0.0
                elif score_cursor_pos > 99.75:
                    score_cursor_pos = 99.75
                if score_pos >= 0.5:
                    if score_pos > 1.0:
                        score_pos = 1.0
                    score_pos = 100 - (score_pos * BAR_SIZE_UNION + 10) / BAR_SIZE_UNION * 100
                    score_cursor = f"<p class=\"p_pos_score\" style=\"right: {score_pos}%;\">" \
                        f"{converted_score}({converted_nb}%) <span class=\"p_pos\"></span></p>"
                else:
                    if score_pos < 0.0:
                        score_pos = 0.0
                    score_pos = (score_pos * BAR_SIZE_UNION - 10) / BAR_SIZE_UNION * 100
                    score_cursor = f"<p class=\"p_pos_score\" style=\"left: {score_pos}%;\">" \
                        f"<span class=\"p_pos\"></span> {converted_score}({converted_nb}%)</p>"

            list_replace_union = [
                ("p_color", "p_" + signal_type),
                ("p_name", unit_data[1]),
                ("p_goon", unit_data[2]),
                ("p_quota", unit_data[3]),
                ("converted_score", converted_score),
                ("converted_nb", converted_nb),
                ("score_cursor", score_cursor),
                ("p_score_pos", score_cursor_pos),
            ]
            list_replace_union += [("h_score_%d" % i, list_cut[i]) for i in range(5)]
            list_replace_union += [("h_nb_%d" % i, list_cut_nb[i]) for i in range(5)]
            list_replace_union += [("h_cut_pos_%d" % i, list_cut_pos[i]) for i in range(5)]
            list_replace_union += [("h_bar_size_%d" % i, list_bar_size[i]) for i in range(5)]

            if is_school_type_union:
                list_replace_union.append(("p_my_score_info",
                                           f"<td class=\"p_mine\">{converted_score}</td>\n" +
                                           f"<td class=\"p_mine\">{converted_nb}%</td>"))
            else:
                if unit_idx % NUMBER_OF_MAJOR_IN_PAGE == 0:
                    list_replace_union.append(("p_my_score_info",
                                               f"<td class=\"p_mine p_mine2\" rowspan={NUMBER_OF_MAJOR_IN_PAGE}>{converted_score}</td>\n" +
                                               f"<td class=\"p_mine\" rowspan={NUMBER_OF_MAJOR_IN_PAGE}>{converted_nb}%</td>"))
                else:
                    list_replace_union.append(("p_my_score_info", ""))

            for replace_target, replace_content in list_replace_union:
                now_p_tr = now_p_tr.replace(replace_target, str(replace_content))
            now_table += now_p_tr
            # 페이지 분할
            if unit_idx != 0 and (unit_idx + 1) % NUMBER_OF_MAJOR_IN_PAGE == 0 or \
                    unit_idx == len(dict_unit_table[school][affiliation]) - 1:
                now_page += p_page.replace("p_tr_section", now_table)
                now_table = ""
        now_page = now_page.replace("school_name", dict_school_name_table[school])
        custom_section += now_nb_page + "\n" + now_page
    template = template.replace("[custom_section]", custom_section)

    # 최하단 footer 생성
    template = template.replace("write_ver", config.app_version) \
                       .replace("write_time", strftime("%B %dth %A %H:%M", localtime())) \
                       .replace("gosok_date", config.gosok_date)

    return template
