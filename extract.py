from BeautifulSoup import BeautifulStoneSoup as bss
from BeautifulSoup import BeautifulSoup as bs
import re
import csv
import codecs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

f = open("ICTRP-Results_long.xml", "r")
f_data = f.readlines()
#delete data after scientific titlech   

x = bs(''.join(f_data))

internal_number =  x('internal_number')
trialid = x('trialid')
last_refreshed_on = x('last_refreshed_on')
public_title = x('public_title')
scientific_title = x('scientific_title')
primary_sponsor = x('primary_sponsor')
date_registration = x('date_registration')
source_register = x('source_register')
web_address = x('web_address')
recruitment_status = x('recruitment_status')
other_records = x('other_records')
inclusion_gender = x('inclusion_gender')
date_enrollement = x('date_enrollement')
target_size = x('target_size')
study_type =  x('study_type')
study_design = x('study_design')
inclusion_criteria = x('inclusion_criteria')
exclusion_criteria = x('exclusion_criteria')
condition = x('condition')
intervention = x('intervention')
primary_outcome = x('primary_outcome')
secondary_id = x('secondary_id')


def shaping_1(x):
    for i in range(len(x)):
        p = re.compile('^[\w|\d|&lt;br&gt;]')
        q = re.compile('&lt;br&gt;')
        p_1 = p.findall(x[i].string)
        x[i].string = p.sub('\n\t'+p_1[0], x[i].string)
        x[i].string = q.sub('\n\t', x[i].string)  

def shaping_2(x):
    for i in range(len(x)):
        p = re.compile('  +')
        x[i].string = p.sub('', x[i].string)

def shaping_3(x):
    for i in range(len(x)):
        p = re.compile('  +')
        x[i].string = p.sub('', x[i].string)

def shaping_4(x):
    for i in range(len(x)):
        p = re.compile('&lt;br&gt;')
        q = re.compile('Male')
        x[i].string = p.sub('', x[i].string)
        x[i].string = q.sub(', Male', x[i].string)


def shaping():
    shaping_1(study_design)
    shaping_1(inclusion_criteria)
    shaping_1(exclusion_criteria)
    shaping_1(condition)
    shaping_1(intervention)
    shaping_1(primary_outcome)
    shaping_2(scientific_title)
    shaping_3(web_address)
    shaping_4(inclusion_gender)

shaping()

def text_output():
    print_obj = ""
    for i in range(len(internal_number)):
        print_obj += """
============================================================
internal_number: %s\n
trialid: %s\n
last refreshed on: %s\n
public_title: %s\n
scientific_title: %s\n
primary_sponsor: %s\n
date_registration: %s\n
source_register: %s\n
web_address: %s\n
recruitment_status: %s\n
other_records: %s\n
inclusion_gender: %s\n
date_enrollement: %s\n
target_size: %s\n
study_type: %s\n
study_design: %s
inclusion_criteria: \t%s
exclusion_criteria: \t%s
condition: \t%s
intervention: \t%s
primary_outcome: \t%s
secondary_id: %s
============================================================
    """ %(
            internal_number[i].string,
            trialid[i].string,
            last_refreshed_on[i].string,
            public_title[i].string,
            scientific_title[i].string,
            primary_sponsor[i].string,
            date_registration[i].string,
            source_register[i].string,
            web_address[i].string,
            recruitment_status[i].string,
            other_records[i].string,
            inclusion_gender[i].string,
            date_enrollement[i].string,
            target_size[i].string,
            study_type[i].string,
            study_design[i].string,
            inclusion_criteria[i].string,
            exclusion_criteria[i].string,
            condition[i].string,
            intervention[i].string,
            primary_outcome[i].string,
            secondary_id[i].string
            )
    f = codecs.open('output.txt', 'w', encoding='utf-8')
    f.write(print_obj)
    f.close()

    return print_obj

def make_csv():
    with open('export.csv', 'wb') as csvfile:
        export = csv.writer(csvfile, delimiter =',')
        export.writerow(['internal_number'] + 
                    ['trialid'] + 
                    ['last_refreshed_on'] + 
                    ['public_title'] + 
                    ['scientific_title'] + 
                    ['primary_sponsor'] + 
                    ['date_registration'] + 
                    ['source_register'] + 
                    ['web_address'] + 
                    ['recruitment_status'] + 
                    ['other_records'] + 
                    ['inclusion_gender'] + 
                    ['date_enrollement'] + 
                    ['target_size'] + 
                    ['study_type'] + 
                    ['study_design'] + 
                    ['inclusion_criteria'] + 
                    ['exclusion_criteria'] + 
                    ['condition'] + 
                    ['intervention'] + 
                    ['primary_outcome'] + 
                    ['secondary_id'])
        for i in range(len(internal_number)):
            export.writerow([internal_number[i].string , 
            trialid[i].string , 
            last_refreshed_on[i].string , 
            public_title[i].string , 
            scientific_title[i].string , 
            primary_sponsor[i].string , 
            date_registration[i].string , 
            source_register[i].string , 
            web_address[i].string , 
            recruitment_status[i].string , 
            other_records[i].string , 
            inclusion_gender[i].string , 
            date_enrollement[i].string , 
            target_size[i].string , 
            study_type[i].string , 
            study_design[i].string , 
            inclusion_criteria[i].string , 
            exclusion_criteria[i].string , 
            condition[i].string , 
            intervention[i].string , 
            primary_outcome[i].string , 
            secondary_id[i].string])
        return export

def coord(x, y, unit=1):
    width, height = A4
    x, y = x * unit, height -  y * unit
    return x, y

def make_pdf():
    width, height = A4
    styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleN.alignment = TA_LEFT
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER

    # Headers
    hdescrpcion = Paragraph('''<b>descrpcion</b>''', styleBH)
    hpartida = Paragraph('''<b>partida</b>''', styleBH)
    hcandidad = Paragraph('''<b>candidad</b>''', styleBH)
    hprecio_unitario = Paragraph('''<b>precio_unitario</b>''', styleBH)
    hprecio_total = Paragraph('''<b>precio_total</b>''', styleBH)

    # Texts
    descrpcion = Paragraph('long paragraph', styleN)
    partida = Paragraph('1', styleN)
    candidad = Paragraph('120', styleN)
    precio_unitario = Paragraph('$52.00', styleN)
    precio_total = Paragraph('$6240.00', styleN)

    data= [[hdescrpcion, hcandidad,hcandidad, hprecio_unitario, hprecio_total],
           [partida, candidad, descrpcion, precio_unitario, precio_total]]

    table = Table(data, colWidths=[2.05 * cm, 2.7 * cm, 5 * cm,
                                   3* cm, 3 * cm])

    table.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ]))

    c = canvas.Canvas("a.pdf", pagesize=A4)
    table.wrapOn(c, width, height)
    table.drawOn(c, *coord(1.8, 9.6, cm))
    c.save()

if __name__ == '__main__':
    text_output()
    #make_csv()
    make_pdf()