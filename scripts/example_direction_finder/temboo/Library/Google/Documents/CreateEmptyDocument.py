# -*- coding: utf-8 -*-

###############################################################################
#
# CreateEmptyDocument
# Create a new, empty document.
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

class CreateEmptyDocument(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateEmptyDocument Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateEmptyDocument, self).__init__(temboo_session, '/Library/Google/Documents/CreateEmptyDocument')


    def new_input_set(self):
        return CreateEmptyDocumentInputSet()

    def _make_result_set(self, result, path):
        return CreateEmptyDocumentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEmptyDocumentChoreographyExecution(session, exec_id, path)

class CreateEmptyDocumentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateEmptyDocument
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) A Google App-specific password that you've generated after enabling 2-Step Verification.)
        """
        super(CreateEmptyDocumentInputSet, self)._set_input('Password', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the new document to create.)
        """
        super(CreateEmptyDocumentInputSet, self)._set_input('Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(CreateEmptyDocumentInputSet, self)._set_input('Username', value)

class CreateEmptyDocumentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateEmptyDocument Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_EditLink(self):
        """
        Retrieve the value for the "EditLink" output from this Choreo execution. (The edit link URL parsed from the Google response.)
        """
        return self._output.get('EditLink', None)
    def get_ResourceID(self):
        """
        Retrieve the value for the "ResourceID" output from this Choreo execution. ((string) The document resource ID returned from Google.)
        """
        return self._output.get('ResourceID', None)

class CreateEmptyDocumentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateEmptyDocumentResultSet(response, path)
