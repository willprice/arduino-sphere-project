# -*- coding: utf-8 -*-

###############################################################################
#
# ListMergeVarDel
# Remove a field name from a MailChimp list.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListMergeVarDel(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListMergeVarDel Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListMergeVarDel, self).__init__(temboo_session, '/Library/MailChimp/ListMergeVarDel')


    def new_input_set(self):
        return ListMergeVarDelInputSet()

    def _make_result_set(self, result, path):
        return ListMergeVarDelResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMergeVarDelChoreographyExecution(session, exec_id, path)

class ListMergeVarDelInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListMergeVarDel
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp.)
        """
        super(ListMergeVarDelInputSet, self)._set_input('APIKey', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the Mailchimp list associated with the merge var you want to delete.)
        """
        super(ListMergeVarDelInputSet, self)._set_input('ListId', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((required, string) Provide a valid merge var tag. A merge var tag can be retrieved by calling listMergeVars() or by logging in to your account.)
        """
        super(ListMergeVarDelInputSet, self)._set_input('Tag', value)

class ListMergeVarDelResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListMergeVarDel Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mailchimp. Returns the string "true" for success and an error description for failures.)
        """
        return self._output.get('Response', None)

class ListMergeVarDelChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListMergeVarDelResultSet(response, path)
