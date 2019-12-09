from flask import Flask
from flask import render_template, request, redirect, url_for, send_file
from shutil import copyfile
import sys
import traceback

from generator import generate_report, convert_html_to_pdf
from database.unit import dict_school_name_table

app = Flask(__name__)


@app.route('/')
def test_url():
    return "HELLO!"


@app.route('/apply', methods=['POST'])
def go_apply():
    def get_param(param):
        return int(request.form[param]) if request.form[param] != '' else 0

    affiliation = "이과" if int(request.form['aff_type']) == 0 else "문과"
    dict_score = {
        "국어": get_param("s1"),
        "영어": get_param("s3"),
        "한국사": get_param("s4"),
    }
    if get_param("math_type") == 0:
        dict_score.update({
            "수학": {
                "수학가형": get_param("s2")
            }
        })
    else:
        dict_score.update({
            "수학": {
                "수학나형": get_param("s2")
            }
        })

    if get_param("tamgu_type") == 0:
        list_science = [prefix + level for level in ["I", "II"] for prefix in ["물리", "화학", "생명과학", "지구과학"]]
        dict_score.update({
            "탐구": {
                list_science[get_param("g1")]: get_param("s5"),
                list_science[get_param("g2")]: get_param("s6")
            }
        })
    else:
        list_social = ["경제", "동아시아사", "법과정치", "사회·문화", "생활과윤리", "세계지리", "세계사", "윤리와사상", "한국지리"]
        dict_score.update({
            "탐구": {
                list_social[get_param("g1")]: get_param("s5"),
                list_social[get_param("g2")]: get_param("s6")
            }
        })
    if get_param("g3") != -1:
        list_foreign = ["독일어I", "러시아어I", "베트남어I", "스페인어I", "아랍어I", "일본어I", "중국어I", "프랑스어I", "한문I"]
        dict_score.update({
            "제2외국어": {
                list_foreign[get_param("g3")]: get_param("s7")
            }
        })

    print(dict_score)
    print(request.form['real_list_school'])

    list_school = request.form['real_list_school'].split(", ")
    for i in range(len(list_school)):
        for key, value in dict_school_name_table.items():
            if value == list_school[i]:
                list_school[i] = key
                break
    try:
        report_html = generate_report(list_school=list_school, affiliation=affiliation, dict_test=dict_score, is_original_score=False)
        fp = open("/tmp/temp.html", 'w', encoding="utf-8")
        fp.write(report_html)
        fp.close()
        copyfile("./docs/templates.css", "/tmp/templates.css")
        convert_html_to_pdf("/tmp/temp.html", "/tmp/Lumiere.pdf")
        return send_file('/tmp/Lumiere.pdf')
    except TypeError:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err_msg = traceback.format_exception(exc_type, exc_value, exc_traceback)
        print('\n'.join([line for line in err_msg]))
        return render_template('TypeError.htm')
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err_msg = traceback.format_exception(exc_type, exc_value, exc_traceback)
        print('\n'.join([line for line in err_msg]))
        return render_template('Exception.htm')


@app.route('/lumiere.css')
def send_lumiere_css():
    return send_file('./templates/lumiere.css')


@app.route('/img/background.jpg')
def send_main_background():
    return send_file('./templates/img/background.jpg')


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.htm'), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')
