from docxtpl import DocxTemplate
import datetime
import pytils
import uuid
import os
from django.conf import settings
from docx import Document

from pet.models import Pet, Treatment
from manufacture.models import OperatingOrganization


def create_card(pet=Pet.objects.first()):
    doc = DocxTemplate(os.path.join(settings.BASE_DIR, 'report/src/card.docx'))
    # filling the date
    day = pytils.dt.ru_strftime("%d", date=datetime.datetime.now())
    month = pytils.dt.ru_strftime("%B", inflected=True, date=datetime.datetime.now())
    year = pytils.dt.ru_strftime("%y")
    context = {}
    if pet.sterilization_date:
        ster_date = pet.sterilization_date
        context['ster_day'] = ster_date.day
        context['ster_month'] = pytils.dt.ru_strftime("%B", inflected=True, date=ster_date)
        context['ster_year'] = ster_date.year
    if pet.work_order_date:
        w_date = pet.work_order_date
        context['w_day'] = w_date.day
        context['w_month'] = pytils.dt.ru_strftime("%B", inflected=True, date=w_date)
        context['w_year'] = w_date.year
    if pet.recipient_date:
        r_date = pet.recipient_date
        context['r_day'] = r_date.day
        context['r_month'] = pytils.dt.ru_strftime("%B", inflected=True, date=r_date)
        context['r_year'] = r_date.year
    if pet.disposals_date:
        d_date = pet.disposals_date
        context['d_day'] = d_date.day
        context['d_month'] = pytils.dt.ru_strftime("%B", inflected=True, date=d_date)
        context['d_year'] = d_date.year
    if pet.accounting_card:
        context['acc_card'] = pet.accounting_card
    if pet.shelter:
        if pet.shelter.address:
            context['sh_address'] = pet.shelter.adress
    if OperatingOrganization.name:
        context['op_org'] = OperatingOrganization.name
    if pet.aviary:
        context['aviary'] = pet.aviary
    if pet.gender:
        context['sex'] = pet.gender
    if pet.breed:
        context['bread'] = pet.breed
    if pet.name:
        context['klich'] = pet.name
    if pet.color:
        context['color'] = pet.color
    if pet.furs_type:
        context['wool'] = pet.furs_type
    if pet.ears_type:
        context['ears'] = pet.ears_type
    if pet.tail_type:
        context['tail'] = pet.tail_type
    if pet.size_type:
        context['size'] = pet.size_type
    if pet.special_parameters:
        context['spec'] = pet.special_parameters
    if pet.id_label:
        context['label'] = pet.id_label
    if pet.work_order:
        context['w_order'] = pet.work_order
    if pet.catching_act:
        context['c_act'] = pet.catching_act
    if pet.catching_address:
        context['c_address'] = pet.catching_address
    if pet.recipient_act:
        context['r_act'] = pet.recipient_act
    if pet.contract_act:
        context['d_act'] = pet.contract_act
    if pet.disposals_cause:
        context['d_cause'] = pet.disposals_cause
    if pet.weight:
        context['weight'] = pet.weight
    context['day'] = day
    context['month'] = month
    context['day'] = year
#    t_date = Treatment.date
#    prep = Treatment.product_name
#    doze = Treatment.dose
#    context = {
#        'tbl_contents': Treatment.number, 'cols': [t_date, prep, doze]
#    }

    # if pet.pet_type.value.lower() == "собака":
    #     tpl.replace_pic('image002.png', 'src/gal.png')
    # else:
    #     tpl.replace_pic('image003.png', 'src/gal.png')

    #doc.replace_media('image2.png', os.path.join(settings.BASE_DIR, 'report/src/gal.png'))
    doc.render(context)

    path = f"static/documents/{uuid.uuid4()}.docx"
    doc.save(os.path.join(settings.BASE_DIR, path))
    return path

#def create_symmary(pet=Pet.objects.first()):
#    doc = DocxTemplate(os.path.join(settings.BASE_DIR, 'report/src/summary.docx'))
#    day = pytils.dt.ru_strftime("%d", date=datetime.datetime.now())
#    month = pytils.dt.ru_strftime("%B", inflected=True, date=datetime.datetime.now())
#    year = pytils.dt.ru_strftime("%y")
#    context = {}