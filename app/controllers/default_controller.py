import connexion
import six

from app.models.inline_response200 import InlineResponse200  # noqa: E501
from app.models.inline_response400 import InlineResponse400  # noqa: E501
from app import util


def root_get():  # noqa: E501
    """root_get

    Returns a blog of COD Mobile # noqa: E501


    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'
