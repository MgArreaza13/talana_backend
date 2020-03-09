import serpy

class PetSerializers(serpy.Serializer):
    
    """
        This class convert tasks data into json
    """
    id = serpy.Field()
    # username = serpy.Field()
    title = serpy.Field()
    description = serpy.Field()
    likes = serpy.Field()
    created = serpy.Field()
    photo =  serpy.MethodField()


    def get_photo(self, obj):
        """
            With this method obtain phone number of the user

            :param obj: object User
            :type obj: Model User
            :return: if phone number is None return None
            :return: phone number
        """
        if obj.photo is None:
            return None
        return obj.photo.url