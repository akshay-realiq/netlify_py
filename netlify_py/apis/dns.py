"""DNS module"""
from netlify_py.apis.api_base import ApiBase


class DNS(ApiBase):
    """
    DNS API Class
    Args:
        access_token (str): netlify access token
        base_url (str): netlify api base url
    """

    def __init__(self, access_token, base_url):
        self._base_url = base_url
        super().__init__(access_token)

    # endpoints
    _site_dns = "sites/{site_id}/dns"
    _dns_zones = "dns_zones"
    _dns_zone = "dns_zones/{zone_id}"
    _transfer_dns_zones = "dns_zones/{zone_id}/transfer"
    _dns_records = "dns_zones/{zone_id}/dns_records"
    _dns_record = \
        "dns_zones/{zone_id}/dns_records/{dns_record_id}"

    # methods
    def list_dns_zones(self):
        """
        List all DNS zones

        Returns:
            list of DNS zones
        """
        return self._get_request(self._base_url + self._dns_zones)

    def get_dns_zone(self, zone_id):
        """
        Get details of a specific DNS zones
        Args:
            zone_id (str): unique zone id
        Returns:
            DNS zone detail
        """
        return self._get_request(self._base_url + self._dns_zone.format(zone_id=zone_id))

    def list_site_dns(self, site_id):
        """
        Get a specific site's DNS
        Args:
            site_id (str): unique site id

        Returns:
            site dns details
        """
        return self._get_request(self._base_url + self._site_dns.format(site_id=site_id))