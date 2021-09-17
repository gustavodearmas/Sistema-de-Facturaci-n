from django.forms import TextInput, Select, EmailInput, ModelForm, Textarea, NumberInput, CheckboxInput, \
    ModelChoiceField
from core.erp.models import Contact, Category, Product, Dptos


class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['client'].widget.attrs['class'] = 'form-check-input'
        self.fields['provider'].widget.attrs['class'] = 'form-check-input'
        self.fields['type_identification'].widget.attrs['class'] = 'form-control k_selectpicker'
        self.fields['type_person'].widget.attrs['class'] = 'form-control k_selectpicker'
        self.fields['type_responsibility'].widget.attrs['class'] = 'form-control k_selectpicker'
        self.fields['country'].widget.attrs['class'] = 'form-control k_selectpicker'
        self.fields['departament'].widget.attrs['class'] = 'form-control k_selectpicker'
        self.fields['city'].widget.attrs['class'] = 'form-control k_selectpicker'

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'type_identification': Select(
                attrs={
                    'placeholder': 'Tipo de identificación'
                }
            ),
            'identification': TextInput(
                attrs={
                    'placeholder': 'Nº de indentificación...',
                }
            ),
            'dv': TextInput(
                attrs={
                    'placeholder': 'Dv...',
                    'style': ' width: 30%;',
                }
            ),
            'name_client_1': TextInput(
                attrs={
                    'placeholder': 'Ingrese el primer nombre...',
                }
            ),
            'name_client_2': TextInput(
                attrs={
                    'placeholder': 'Ingrese el segundo nombre...',
                }
            ),
            'last_names_cliente': TextInput(
                attrs={
                    'placeholder': 'Ingrese los apellidos...',
                }
            ),
            'type_person': Select(
                attrs={
                    'placeholder': 'Tipo de persona...',
                }
            ),
            'type_responsibility': Select(
                attrs={
                    'placeholder': 'Tipo de resposabilidad...',
                }
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Ingrese la dirección...',
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': 'Ingrese el email...',
                }
            ),
            'tel_1': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nº de teléfono...',
                }
            ),
            'tel_2': TextInput(
                attrs={
                    'placeholder': 'Opcional...',
                }
            ),
            'mobile': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nº de celular...',
                }
            ),
        }


    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    #Aquí se agregan validaciones adicionales
    def clean(self):
        cleaned = super().clean()
        #if len(cleaned['dv']) >= 2:
        #raise forms.ValidationError('Error de prueba')
        #self.add_error('dv', 'El número de verificación, solo puede tener dos números. Por favor, verifique su información. ')
        #print(cleaned)
        return cleaned

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Nombre de la categoría'
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Descripción'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['cate'].widget.attrs['class'] = 'form-control k_selectpicker'
        self.fields['inventory'].widget.attrs['class'] = 'form-check-input'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
        self.fields['image'].widget.attrs['id'] = 'customFile'

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Nombre del producto'
                }
            ),
            'reference': TextInput(
                attrs={
                    'placeholder': 'Número de referencia'
                }
            ),
            'cate': Select(
                attrs={
                    'placeholder': 'Categoría'
                }
            ),
            'cost': NumberInput(
                attrs={
                    'placeholder': 'Precio de costo'
                }
            ),
            'price': NumberInput(
                attrs={
                    'placeholder': 'Precio de venta'
                }
            ),
            'description': TextInput(
                attrs={
                    'placeholder': 'Descripcón'
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

#Borrar
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'type_identification': Select(
                attrs={
                    'placeholder': 'Tipo de identificación'
                }
            ),
            'identification': TextInput(
                attrs={
                    'placeholder': 'Nº de indentificación...',
                }
            ),
            'dv': TextInput(
                attrs={
                    'placeholder': 'Dv...',
                    'style': ' width: 30%;',
                }
            ),
            'name_client_1': TextInput(
                attrs={
                    'placeholder': 'Ingrese el primer nombre...',
                }
            ),
            'name_client_2': TextInput(
                attrs={
                    'placeholder': 'Ingrese el segundo nombre...',
                }
            ),
            'last_names_cliente': TextInput(
                attrs={
                    'placeholder': 'Ingrese los apellidos...',
                }
            ),
            'type_person': Select(
                attrs={
                    'placeholder': 'Tipo de persona...',
                }
            ),
            'type_responsibility': Select(
                attrs={
                    'placeholder': 'Tipo de resposabilidad...',
                }
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Ingrese la dirección...',
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': 'Ingrese el email...',
                }
            ),
            'tel_1': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nº de teléfono...',
                }
            ),
            'tel_2': TextInput(
                attrs={
                    'placeholder': 'Opcional...',
                }
            ),
            'mobile': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nº de celular...',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departament'].queryset = Dptos.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['departament'].queryset = Dptos.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['departament'].queryset = self.instance.country.city_set.order_by('name')