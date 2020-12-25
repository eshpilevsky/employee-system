from django.contrib import admin
from django.contrib.gis.db.models import PointField

from mapwidgets import GooglePointFieldWidget

from employee.models import Employee, Branch


class InputFilter(admin.SimpleListFilter):
    template = "admin/input_filter.html"

    def lookups(self, request, model_admin):
        return ((),)

    def choices(self, changelist):
        all_choice = next(super().choices(changelist))
        all_choice["query_parts"] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice


class FirstNameFilter(InputFilter):
    parameter_name = "first_name"
    title = "First Name"

    def queryset(self, request, queryset):
        if self.value() is not None:
            first_name = self.value()
            return queryset.filter(first_name=first_name)


class LastNameFilter(InputFilter):
    parameter_name = "last_name"
    title = "Last Name"

    def queryset(self, request, queryset):
        if self.value() is not None:
            last_name = self.value()
            return queryset.filter(last_name=last_name)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "position_title")
    search_fields = ("first_name", "last_name")
    list_filter = (FirstNameFilter, LastNameFilter)


class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "image_tag", "get_position", "get_employees")
    readonly_fields = ["image_tag"]

    def get_employees(self, obj: Branch):
        return ", ".join([f"{e.first_name} {e.last_name}" for e in obj.employees.all()])

    def get_position(self, obj: Branch):
        return obj.position.coords

    formfield_overrides = {PointField: {"widget": GooglePointFieldWidget}}

    get_employees.short_description = "Employees"
    get_position.short_description = "Position"


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Branch, BranchAdmin)
