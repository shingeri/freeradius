"""Test VLAN."""
import __config__
normal = __config__.VLAN("dev", 10)
admin_only = __config__.VLAN("prod", 11)
