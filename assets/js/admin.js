/* global angular */

import { AdminController } from './adminController';
import { EditController } from './editController';

var app = angular.module('AdminApp', ['jsonFormatter']);

app.controller('AdminController', AdminController);
app.controller('EditController', EditController);