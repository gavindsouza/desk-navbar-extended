import frappe

NAVBAR_ITEM_LABEL = "Show Time"
NAVBAR_EXTND_ITEMS = [
    {
        "item_label": NAVBAR_ITEM_LABEL,
        "item_type": "Action",
        "action": "() => {}",
        "idx": 1,
    },
    {
        "item_type": "Separator",
        "idx": 2,
    },
]


def after_install():
    if frappe.db.exists("Navbar Item", {"item_label": NAVBAR_ITEM_LABEL}):
        return

    navbar_settings = frappe.get_single("Navbar Settings")
    for ni in navbar_settings.settings_dropdown:
        ni.idx = ni.idx + len(NAVBAR_EXTND_ITEMS)
    navbar_settings.extend("settings_dropdown", NAVBAR_EXTND_ITEMS)
    navbar_settings.save()
    frappe.db.commit()


def after_uninstall():
    if not frappe.db.exists("Navbar Item", {"item_label": NAVBAR_ITEM_LABEL}):
        return

    patch_flag = frappe.flags.in_patch
    frappe.flags.in_patch = True
    navbar_settings = frappe.get_single("Navbar Settings")

    for i, ni in enumerate(navbar_settings.settings_dropdown):
        if ni.item_label == NAVBAR_ITEM_LABEL:
            navbar_settings.settings_dropdown.pop(i)
            if navbar_settings.settings_dropdown[i + 1].item_stype == "Separator":
                navbar_settings.settings_dropdown.pop(i + 1)
            break
    navbar_settings.save()
    frappe.db.commit()
    frappe.flags.in_patch = patch_flag
