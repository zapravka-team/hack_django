from django.db.models import Q

from .models import Pet

PET_FIELDS = Pet.get_field_names()

PET_BASE_FIELDS = ('name', 'color', 'bread')
PET_TYPE_FIELDS = set(Pet.get_type_filed_names())
print(PET_TYPE_FIELDS)
FILTERING_FIELDS = ('name', 'weight', 'gender',)
REQUEST_PARAMS = {'type', 'count', 'offset', 'filter', 'search'}
REGEX_SEARCHING_FIELDS = ('name',)

DEFAULT_LIMIT = 100


class ValidationError(Exception):
    pass


class ExcessParam(Exception):
    def __init__(self, *args, param):
        self.param = param
        super().__init__(*args)


class ExcessFiled(Exception):
    def __init__(self, *args, field):
        self.field = field
        super().__init__(*args)


def normalize_pet_query_request(request_data):
    normalized_req = {}
    if len(set(request_data.keys()) - REQUEST_PARAMS) != 0:
        raise ExcessParam(param='debug')

    try:
        if request_data['type'] == 'base':
            normalized_req['fields'] = list(PET_BASE_FIELDS)
        elif request_data['type'] == 'base':
            normalized_req['fields'] = list(PET_FIELDS)
    except KeyError:
        raise ValidationError("param 'type' must be specified")

    try:
        normalized_req['count'] = int(request_data.get('count', DEFAULT_LIMIT))
        normalized_req['offset'] = int(request_data.get('offset', 0))
    except ValueError:
        raise ValidationError('count and offset must be int ')

    req_filter = request_data.get('filter', {})
    for field, values in req_filter.items():
        if field not in PET_FIELDS:
            raise ExcessFiled(field=field)
        if not isinstance(values, list):
            raise ValidationError('values of fields must be list')
        if len(values) == 0:
            raise ValidationError('values cant be empty')
    normalized_req['filter'] = req_filter
    normalized_req['search'] = request_data.get('search')
    normalized_req['sort'] = request_data.get('sort')
    normalized_req['require_socialized'] = False
    return normalized_req


def get_pet_query(nor_req, managing_filter=Q()):
    filter_exp = managing_filter
    for field, values in nor_req['filter'].items():
        if field in PET_TYPE_FIELDS:
            field += '__value'
        if len(values) > 1:
            field += '__in'
            filter_exp &= Q(**{field: values})
        else:
            filter_exp &= Q(**{field: values[0]})
    if nor_req['search'] is not None:
        for field in REGEX_SEARCHING_FIELDS:
            filter_exp &= Q(**{f'{field}__regex': nor_req['search']})

    offset = nor_req['offset']
    count = nor_req['count']
    offset_count = slice(offset, count)
    sorting = 'id'
    if nor_req['sort'] is not None:
        sorting = nor_req['sort']

    # special_values = []
    # for field in nor_req['fields']:
    #     if field in PET_TYPE_FIELDS:
    #         special_values.append(f'{field}__value')
    #     else:
    #         special_values.append(field)
    return Pet.objects.filter(filter_exp).order_by(sorting)[offset_count]
