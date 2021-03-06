# -*- coding: utf-8 -*-

###############################################################################
#
# ClientLoginAuthentication
# Request an authorization token for Google Documents.
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

class ClientLoginAuthentication(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ClientLoginAuthentication Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ClientLoginAuthentication, self).__init__(temboo_session, '/Library/Google/Spreadsheets/ClientLoginAuthentication')


    def new_input_set(self):
        return ClientLoginAuthenticationInputSet()

    def _make_result_set(self, result, path):
        return ClientLoginAuthenticationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ClientLoginAuthenticationChoreographyExecution(session, exec_id, path)

class ClientLoginAuthenticationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ClientLoginAuthentication
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) A Google App-specific password that you've generated after enabling 2-Step Verification.)
        """
        super(ClientLoginAuthenticationInputSet, self)._set_input('Password', value)
    def set_Service(self, value):
        """
        Set the value of the Service input for this Choreo. ((required, string) The service that you are requesting an authorization token for. Defaults to 'wise' for Spreadsheets API.)
        """
        super(ClientLoginAuthenticationInputSet, self)._set_input('Service', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(ClientLoginAuthenticationInputSet, self)._set_input('Username', value)

class ClientLoginAuthenticationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ClientLoginAuthentication Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_AuthorizationKey(self):
        """
        Retrieve the value for the "AuthorizationKey" output from this Choreo execution. ((string) The auth token parsed from the Google login response)
        """
        return self._output.get('AuthorizationKey', None)

class ClientLoginAuthenticationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ClientLoginAuthenticationResultSet(response, path)
