/* global angular */

import { initUI } from './admin.ui';
import { DashboardController } from './dashboard.view';
import { ViewNamespaceController } from './namespace.view';
import { ViewSubmissionController } from './submissions.view';
import { ListSubmissionController } from './submissions.list';
import { AddNamespaceController } from './namespace.add';
import { AddBlurbController } from './blurbs.add';

// initialize UI
initUI();

var app = angular.module('AdminApp', ['jsonFormatter', 'googlechart']);

app.controller('DashboardController', DashboardController);
app.controller('ViewSubmissionController', ViewSubmissionController);
app.controller('ListSubmissionController', ListSubmissionController);
app.controller('AddNamespaceController', AddNamespaceController);
app.controller('ViewNamespaceController', ViewNamespaceController);
app.controller('AddBlurbController', AddBlurbController);