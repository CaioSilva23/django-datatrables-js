from django.template import Library


register = Library()


@register.filter('formata_preco')
def formata_preco(value):
    return f"R$ {value:_.2f}".replace('.',',').replace('_','.')



@register.filter('formata_percent')
def formata_percent(value):
    return f"{value:.2f}%"

