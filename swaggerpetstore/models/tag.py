# -*- coding: utf-8 -*-

"""
swaggerpetstore

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerpetstore.api_helper import APIHelper


class Tag(object):

    """Implementation of the 'Tag' model.

    TODO: type model description here.

    Attributes:
        id (long|int): TODO: type description here.
        photo_urls (list of string): TODO: type description here.
        name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "photo_urls": 'photoUrls',
        "id": 'id',
        "name": 'name'
    }

    _optionals = [
        'id',
        'name',
    ]

    def __init__(self,
                 photo_urls=None,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP):
        """Constructor for the Tag class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        self.photo_urls = photo_urls 
        if name is not APIHelper.SKIP:
            self.name = name 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        photo_urls = dictionary.get("photoUrls") if dictionary.get("photoUrls") else None
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        # Return an object of this model
        return cls(photo_urls,
                   id,
                   name)