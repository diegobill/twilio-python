r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, List, Optional, Union
from twilio.base import serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ComplianceTollfreeInquiriesInstance(InstanceResource):
    class OptInType(object):
        VERBAL = "VERBAL"
        WEB_FORM = "WEB_FORM"
        PAPER_FORM = "PAPER_FORM"
        VIA_TEXT = "VIA_TEXT"
        MOBILE_QR_CODE = "MOBILE_QR_CODE"

    """
    :ivar inquiry_id: The unique ID used to start an embedded compliance registration session.
    :ivar inquiry_session_token: The session token used to start an embedded compliance registration session.
    :ivar registration_id: The TolfreeId matching the Tollfree Profile that should be resumed or resubmitted for editing.
    :ivar url: The URL of this resource.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.inquiry_id: Optional[str] = payload.get("inquiry_id")
        self.inquiry_session_token: Optional[str] = payload.get("inquiry_session_token")
        self.registration_id: Optional[str] = payload.get("registration_id")
        self.url: Optional[str] = payload.get("url")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Trusthub.V1.ComplianceTollfreeInquiriesInstance>"


class ComplianceTollfreeInquiriesList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ComplianceTollfreeInquiriesList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/ComplianceInquiries/Tollfree/Initialize"

    def create(
        self,
        tollfree_phone_number: str,
        notification_email: str,
        business_name: Union[str, object] = values.unset,
        business_website: Union[str, object] = values.unset,
        use_case_categories: Union[List[str], object] = values.unset,
        use_case_summary: Union[str, object] = values.unset,
        production_message_sample: Union[str, object] = values.unset,
        opt_in_image_urls: Union[List[str], object] = values.unset,
        opt_in_type: Union[
            "ComplianceTollfreeInquiriesInstance.OptInType", object
        ] = values.unset,
        message_volume: Union[str, object] = values.unset,
        business_street_address: Union[str, object] = values.unset,
        business_street_address2: Union[str, object] = values.unset,
        business_city: Union[str, object] = values.unset,
        business_state_province_region: Union[str, object] = values.unset,
        business_postal_code: Union[str, object] = values.unset,
        business_country: Union[str, object] = values.unset,
        additional_information: Union[str, object] = values.unset,
        business_contact_first_name: Union[str, object] = values.unset,
        business_contact_last_name: Union[str, object] = values.unset,
        business_contact_email: Union[str, object] = values.unset,
        business_contact_phone: Union[str, object] = values.unset,
    ) -> ComplianceTollfreeInquiriesInstance:
        """
        Create the ComplianceTollfreeInquiriesInstance

        :param tollfree_phone_number: The Tollfree phone number to be verified
        :param notification_email: The email address to receive the notification about the verification result.
        :param business_name: The name of the business or organization using the Tollfree number.
        :param business_website: The website of the business or organization using the Tollfree number.
        :param use_case_categories: The category of the use case for the Tollfree Number. List as many are applicable..
        :param use_case_summary: Use this to further explain how messaging is used by the business or organization.
        :param production_message_sample: An example of message content, i.e. a sample message.
        :param opt_in_image_urls: Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
        :param opt_in_type:
        :param message_volume: Estimate monthly volume of messages from the Tollfree Number.
        :param business_street_address: The address of the business or organization using the Tollfree number.
        :param business_street_address2: The address of the business or organization using the Tollfree number.
        :param business_city: The city of the business or organization using the Tollfree number.
        :param business_state_province_region: The state/province/region of the business or organization using the Tollfree number.
        :param business_postal_code: The postal code of the business or organization using the Tollfree number.
        :param business_country: The country of the business or organization using the Tollfree number.
        :param additional_information: Additional information to be provided for verification.
        :param business_contact_first_name: The first name of the contact for the business or organization using the Tollfree number.
        :param business_contact_last_name: The last name of the contact for the business or organization using the Tollfree number.
        :param business_contact_email: The email address of the contact for the business or organization using the Tollfree number.
        :param business_contact_phone: The phone number of the contact for the business or organization using the Tollfree number.

        :returns: The created ComplianceTollfreeInquiriesInstance
        """
        data = values.of(
            {
                "TollfreePhoneNumber": tollfree_phone_number,
                "NotificationEmail": notification_email,
                "BusinessName": business_name,
                "BusinessWebsite": business_website,
                "UseCaseCategories": serialize.map(use_case_categories, lambda e: e),
                "UseCaseSummary": use_case_summary,
                "ProductionMessageSample": production_message_sample,
                "OptInImageUrls": serialize.map(opt_in_image_urls, lambda e: e),
                "OptInType": opt_in_type,
                "MessageVolume": message_volume,
                "BusinessStreetAddress": business_street_address,
                "BusinessStreetAddress2": business_street_address2,
                "BusinessCity": business_city,
                "BusinessStateProvinceRegion": business_state_province_region,
                "BusinessPostalCode": business_postal_code,
                "BusinessCountry": business_country,
                "AdditionalInformation": additional_information,
                "BusinessContactFirstName": business_contact_first_name,
                "BusinessContactLastName": business_contact_last_name,
                "BusinessContactEmail": business_contact_email,
                "BusinessContactPhone": business_contact_phone,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ComplianceTollfreeInquiriesInstance(self._version, payload)

    async def create_async(
        self,
        tollfree_phone_number: str,
        notification_email: str,
        business_name: Union[str, object] = values.unset,
        business_website: Union[str, object] = values.unset,
        use_case_categories: Union[List[str], object] = values.unset,
        use_case_summary: Union[str, object] = values.unset,
        production_message_sample: Union[str, object] = values.unset,
        opt_in_image_urls: Union[List[str], object] = values.unset,
        opt_in_type: Union[
            "ComplianceTollfreeInquiriesInstance.OptInType", object
        ] = values.unset,
        message_volume: Union[str, object] = values.unset,
        business_street_address: Union[str, object] = values.unset,
        business_street_address2: Union[str, object] = values.unset,
        business_city: Union[str, object] = values.unset,
        business_state_province_region: Union[str, object] = values.unset,
        business_postal_code: Union[str, object] = values.unset,
        business_country: Union[str, object] = values.unset,
        additional_information: Union[str, object] = values.unset,
        business_contact_first_name: Union[str, object] = values.unset,
        business_contact_last_name: Union[str, object] = values.unset,
        business_contact_email: Union[str, object] = values.unset,
        business_contact_phone: Union[str, object] = values.unset,
    ) -> ComplianceTollfreeInquiriesInstance:
        """
        Asynchronously create the ComplianceTollfreeInquiriesInstance

        :param tollfree_phone_number: The Tollfree phone number to be verified
        :param notification_email: The email address to receive the notification about the verification result.
        :param business_name: The name of the business or organization using the Tollfree number.
        :param business_website: The website of the business or organization using the Tollfree number.
        :param use_case_categories: The category of the use case for the Tollfree Number. List as many are applicable..
        :param use_case_summary: Use this to further explain how messaging is used by the business or organization.
        :param production_message_sample: An example of message content, i.e. a sample message.
        :param opt_in_image_urls: Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
        :param opt_in_type:
        :param message_volume: Estimate monthly volume of messages from the Tollfree Number.
        :param business_street_address: The address of the business or organization using the Tollfree number.
        :param business_street_address2: The address of the business or organization using the Tollfree number.
        :param business_city: The city of the business or organization using the Tollfree number.
        :param business_state_province_region: The state/province/region of the business or organization using the Tollfree number.
        :param business_postal_code: The postal code of the business or organization using the Tollfree number.
        :param business_country: The country of the business or organization using the Tollfree number.
        :param additional_information: Additional information to be provided for verification.
        :param business_contact_first_name: The first name of the contact for the business or organization using the Tollfree number.
        :param business_contact_last_name: The last name of the contact for the business or organization using the Tollfree number.
        :param business_contact_email: The email address of the contact for the business or organization using the Tollfree number.
        :param business_contact_phone: The phone number of the contact for the business or organization using the Tollfree number.

        :returns: The created ComplianceTollfreeInquiriesInstance
        """
        data = values.of(
            {
                "TollfreePhoneNumber": tollfree_phone_number,
                "NotificationEmail": notification_email,
                "BusinessName": business_name,
                "BusinessWebsite": business_website,
                "UseCaseCategories": serialize.map(use_case_categories, lambda e: e),
                "UseCaseSummary": use_case_summary,
                "ProductionMessageSample": production_message_sample,
                "OptInImageUrls": serialize.map(opt_in_image_urls, lambda e: e),
                "OptInType": opt_in_type,
                "MessageVolume": message_volume,
                "BusinessStreetAddress": business_street_address,
                "BusinessStreetAddress2": business_street_address2,
                "BusinessCity": business_city,
                "BusinessStateProvinceRegion": business_state_province_region,
                "BusinessPostalCode": business_postal_code,
                "BusinessCountry": business_country,
                "AdditionalInformation": additional_information,
                "BusinessContactFirstName": business_contact_first_name,
                "BusinessContactLastName": business_contact_last_name,
                "BusinessContactEmail": business_contact_email,
                "BusinessContactPhone": business_contact_phone,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ComplianceTollfreeInquiriesInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trusthub.V1.ComplianceTollfreeInquiriesList>"
