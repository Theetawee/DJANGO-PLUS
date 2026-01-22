from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    # add_form = AccountCreationForm

    list_display = (
        "username",
        "email_address",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = (
        "username",
        "email_address",
    )
    readonly_fields = ("last_login", "date_joined")
    ordering = ("-date_joined",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "username",
                    "email_address",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email_address",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(Account, AccountAdmin)
