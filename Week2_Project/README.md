![Downloads](https://img.shields.io/github/downloads/gitextensions/gitextensions/v2.51/total.svg)

#### Features:
* Commandline difftool raised Assert - PR [4386]
* Replace lightbulb images - PR [4351]
* Rename arguments related to diff to firstRevision, secondRevision to … - PR [4344]
* Use built-in stream.CopyTo method in SynchronizedProcessReader - PR [4343]
* Add icons in the browse form command menu - PR [4331]
* Display some missing shortcuts in Browse form menus - PR [4330]
* FormBrowse: Add option to display reflog references - PR [4321]
* Display branch name in bold only when it is the one checked out - PR [4320]
* Create branch modal buttons under linux/mono - Issue [4319]
* Browse Diff Untracked: Delete and Edit menu items are not enabled - PR [4318]
* Commit & Push (forced with lease) when Amend is checked - Issue [4296]
* FileHistory: Show Blame tab also for artificial commits - PR [4293]
* Artificial commit changed count should be dynamic - PR [4209]
* Jenkins build server integration: support for multi pipeline and wildcards  - Issue [4202]
* GitEx does not remember splitter position - Issue [4058]
* Enhanced view of uncommitted changes in Browse Repository - Issue [4031]
* Support github-mac:// protocol - Issue [4276]
* Add --simplify-merges when showing file full history - Issue [4264]
* Change text in settings for artificial commits - PR [4246]
* refactor: Split state and behavior of CommitInformation - PR [4241]
* RevisionHeader work follow up - Issue [4237]
* Scroll commit list during rebase conflict so the next to apply commit is visible - Issue [4233]
* Bitbucket basic functionality [#4204] - PR [4228]
* Change the display name for Bitbucket Server plugin - PR [4227]
* Pad fields in RevisionHeader with spaces instead of tabs - PR [4218]
* Bitbucket plugin: Exception if not initialized - PR [4211]
* Rename "Atlassian Stash" to Bitbucket - PR [4210]
* Browse Difftool Menu Items cleanup - PR [4207]
* Jenkins integration - show more interesting data first. - PR [4197]
* Provide GPG tab layout for Mono - Issue [4196]
* Commit Form: Display current branch name - PR [4189]
* Better naming of archives done through a filetree directory - PR [4188]
* BrowseDiff Hotkey support: DEL to delete unstaged files - PR [4168]
* Browse Diff Menu Items should be disabled when no item is SelectedDiff - PR [4167]
* FormBrowse Commands in toolbar menu raised exceptions for artificial … - PR [4166]
* RevisionFileTree context menu gave exceptions if no items were Selected - PR [4165]
* Commit menus raised exceptions if no items were Selected - PR [4163]
* Compare artificial commits to all other commits - PR [4157]
* Always show artificial commits in RevisionGrid - PR [4147]
* View stash - names are cut off and selectfield is not resizable - Issue [4120]
* Fix FormCommit file list filter input getting treated as hotkeys - PR [4115]
* Fix potential copy-paste bug - PR [4109]
* FileHistory: Show DiffTab when opening, not ViewFile - PR [4105]
* Hide CommitInfo panel for virtual commits - PR [4096]
* (A lot of) filetree improvements - PR [4093]
* Browse Diff Submodule menu options for unstaged commit - PR [4092]
* Remove "(slow!)" for showing stageged/unstaged as commits in Settings - PR [4088]
* Stage/unstage in browse - PR [4087]
* Show count for artificial commits - PR [4086]
* CA2202 CA2213 suppression - PR [4085]
* Various forms: limit menu options for artificial and submodule - PR [4084]
* Feature/n4031 refactoring anon icon menu - PR [4079]
* Use GitExt icon for menu items that open a new instance for Submodule - PR [4076]
* Try to find ssh.exe in git installation directory - PR [4074]
* Change "reset all changes" button position in commit dialog - Issue [4057]
* FileStatusList had useless horizontal scrollbar - PR [4052]
* Enhanced view of uncommitted changes in Browse Repository - Issue [4031]
* Enhance file tree control - PR [4022]
* Extract "File Tree" control from FormBrowse - PR [4020]
* Opening up the search dropdown list on focus - Issue [4016]
* Remove RSS feeds functionality - PR [4008]
* "Check for update" window appears behind other open windows - Issue [3999]
* Change Pull dialog title and menu entry to Pull/Fetch - Issue [3970]
* added *.m for Matlab files - PR [3955]
* Reflog: display also reflog for remotes - PR [3953]
* Convert user-supplied relative path to absolute path - Issue [3947]
* Fix tab order in the FileStatusList component - PR [3930]
* Skip worktree feature - PR [3921]
* Form commit workflow improvements - PR [3920]
* Add (and refactor) diff and merge tools - PR [3919]
* Delete index.lock should delete in submodules - Issue [3915]
* Allow to configure the number of Recent repositories - Issue [3908]
* Feature request: Add option to choose branch name ordering preference - Issue [3907]
* Update Reactive Extensions to 3.1 - PR [3900]
* Creating new local branch triggers updating submodules? - Issue [3899]
* On "Commit dialog" configuration page, raise the "previous messages" limit - Issue [3892]
* Feature Req.: Commit button should indicate if file in repos. changed - Issue [3887]
* [Feature] Tag dialog allow to sign the tag - Issue [3842]
* Annoying closing of menu from tool bar buttons - Issue [3832]
* Turn off zebra striping in 2.50 browser? - Issue [3810]
* Make autocomplete for files starting with a dot available in commit message field (in UI of executable) - Issue [3760]
* FormOpenDirectory: Add a button to go (easily) to the parent directory - PR [3733]
* [feature request] More descriptive diffs for merge commits - Issue [3709]
* Add Visual Studio Code to the editor list - Issue [3652]
* Implement support for --skip-worktree - Issue [3525]
* Support signing commits via GPG - Issue [3161]
* Diff window: configurable column for "ruler" or "gutter mark" - Issue [2868]
* Visual Studio 2008: File history/blame shows the current line  - Issue [2839]
* Jira Commit Hint Plugin - PR [2495]
* Context menu for commit with remote branch doesn't offer `Delete branch` option - Issue [1583]

#### Fixes:
* Commit view shows inverted diff output - Issue [4374]
* Wrong diff for stashed untracked files - Issue [4373]
* Branch filtering not working - Issue [4370]
* Unable to add remote having selected deactivated item - Issue [4349]
* Bitbucket Server: XSRF error when approving - Issue [4345]
* fix: AE when starting app without a repository - PR [4340]
* BuildReport: Exception for WebBrowserCtrl.Navigate - Issue [4322]
* Browse Diff Untracked: Delete and Edit menu items are not enabled - Issue [4316]
* FormFileHistory: DiffToLocal hidden also when relevant - Issue [4315]
* Browse Diff Garbage and exception for untracked files - Issue [4301]
* Number of changed files isn't displayed in Commit button - Issue [4295]
* File rename events are not detected by filewatcher - Issue [4292]
* Exception occurs when trying load the delete tag form - Issue [4283]
* "View Stash" triggers System.ArgumentOutOfRangeException - Issue [4263]
* NRE in FormPull when running TranslationApp - Issue [4258]
* Commit tab: _commitInformationProvider was null. - Issue [4255]
* System.IO.IOException "Unable to remove the file to be replaced." - Issue [4250]
* Diff tab selected when GE starts up - Issue [4242]
* puttykeyfile option is not written to config during clone - Issue [4235]
* Commands are duplicated in GE Gitcommand log - Issue [4213]
* BitBucket plugin is broken - Issue [4204]
* Jenkins integration does not refresh "in progress" builds info. - Issue [4185]
* NPE on closing settings dialog - Issue [4160]
* Invisible "Browse" button in "Open repository" dialog - Issue [4132]
* diff.submodules=log raises exception - Issue [4130]
* AOORE in "Open local repository" dialog under Mono - Issue [4126]
* Some commands throws NullReferenceException for a new empty repo (2.50.02) - Issue [4098]
* Debug builds fails at commit if reallocated - PR [4075]
* Unable to filter file in the commit dialog - Issue [4062]
* DiffMerge should be sgdm.exe - Issue [4049]
* Release Notes Generator breaks under git version 2.14.1 - Issue [4028]
* Not able to read TAGMESSAGE file - Issue [4025]
* Github > View pull requests... > Close throws "Object reference not set to an instance of an object." - Issue [4024]
* Cancelling checking if shell extension is registered crashes GitExtensions - PR [4019]
* Filter branch combobox is case sensitive  - Issue [4014]
* NRE on open gitextensions - Issue [4012]
* Scripts with On event setting "AfterCheckout" or "BeforeCheckout" do not activate on revision checkout - Issue [4006]
* Weird tab field order - Issue [3990]
* Commit window title does not reflect newly created branch - Issue [3982]
* Panel layouts are unstable now - Issue [3966]
* NRE when jira plugin not configured - Issue [3962]
* OutOfMemoryException on startup after Changing Commit View Layout - Issue [3959]
* Commit dialog shows unsupported file for sub-modules with diff.mnemonicprefix=true - Issue [3948]
* commit message template file not found in root folder of repo - Issue [3897]
* File tree no longer working - Issue [3875]
* Apply patch / Select patch file should filter for lowercase *.patch - Issue [3867]
* Text strings for `.git/info/exclude` modals need adjusting - Issue [3860]
* "Existing worktrees" window does not handle worktrees with a space in the path - Issue [3849]
* GitFlow plugin is missing since GitExtensions v2.49.03 - Issue [3839]
* Height of bottom tab control (Commit-Info, File-Tree, Diff) gets smaller on GitExtensions start - Issue [3822]
* Fix spelling in UI: "mergeconflict*" -> "merge conflict*" - PR [3772]
* Exception shown instead of error message for locked file in commit dialog - Issue [3759]
* 'Show remote branches' check state does not toggle after click - Issue [3730]
* Multiple GUI regressions on mono - Issue [3725]
* GitCommands: Avoid creating a fake remote ref on pull - PR [3484]
* Format patch creates a file with a lower case p in .patch. Filter uses upper case p in .Patch - Issue [2870]
* Scripts not asking for confirmation even if configured to do so - Issue [1608]
* Show an error message when cloning without specifying a destination - Issue [1605]
* Error while resetting files - Issue [1307]


[4292]:https://github.com/gitextensions/gitextensions/issues/4292
[4283]:https://github.com/gitextensions/gitextensions/issues/4283
[4276]:https://github.com/gitextensions/gitextensions/issues/4276
[4264]:https://github.com/gitextensions/gitextensions/issues/4264
[4263]:https://github.com/gitextensions/gitextensions/issues/4263
[4258]:https://github.com/gitextensions/gitextensions/issues/4258
[4255]:https://github.com/gitextensions/gitextensions/issues/4255
[4250]:https://github.com/gitextensions/gitextensions/issues/4250
[4246]:https://github.com/gitextensions/gitextensions/pull/4246
[4242]:https://github.com/gitextensions/gitextensions/issues/4242
[4241]:https://github.com/gitextensions/gitextensions/pull/4241
[4237]:https://github.com/gitextensions/gitextensions/issues/4237
[4235]:https://github.com/gitextensions/gitextensions/issues/4235
[4233]:https://github.com/gitextensions/gitextensions/issues/4233
[4228]:https://github.com/gitextensions/gitextensions/pull/4228
[4227]:https://github.com/gitextensions/gitextensions/pull/4227
[4218]:https://github.com/gitextensions/gitextensions/pull/4218
[4213]:https://github.com/gitextensions/gitextensions/issues/4213
[4211]:https://github.com/gitextensions/gitextensions/pull/4211
[4210]:https://github.com/gitextensions/gitextensions/pull/4210
[4207]:https://github.com/gitextensions/gitextensions/pull/4207
[4204]:https://github.com/gitextensions/gitextensions/issues/4204
[4197]:https://github.com/gitextensions/gitextensions/pull/4197
[4196]:https://github.com/gitextensions/gitextensions/issues/4196
[4189]:https://github.com/gitextensions/gitextensions/pull/4189
[4188]:https://github.com/gitextensions/gitextensions/pull/4188
[4185]:https://github.com/gitextensions/gitextensions/issues/4185
[4168]:https://github.com/gitextensions/gitextensions/pull/4168
[4167]:https://github.com/gitextensions/gitextensions/pull/4167
[4166]:https://github.com/gitextensions/gitextensions/pull/4166
[4165]:https://github.com/gitextensions/gitextensions/pull/4165
[4163]:https://github.com/gitextensions/gitextensions/pull/4163
[4160]:https://github.com/gitextensions/gitextensions/issues/4160
[4157]:https://github.com/gitextensions/gitextensions/pull/4157
[4147]:https://github.com/gitextensions/gitextensions/pull/4147
[4132]:https://github.com/gitextensions/gitextensions/issues/4132
[4130]:https://github.com/gitextensions/gitextensions/issues/4130
[4126]:https://github.com/gitextensions/gitextensions/issues/4126
[4120]:https://github.com/gitextensions/gitextensions/issues/4120
[4115]:https://github.com/gitextensions/gitextensions/pull/4115
[4109]:https://github.com/gitextensions/gitextensions/pull/4109
[4105]:https://github.com/gitextensions/gitextensions/pull/4105
[4098]:https://github.com/gitextensions/gitextensions/issues/4098
[4096]:https://github.com/gitextensions/gitextensions/pull/4096
[4093]:https://github.com/gitextensions/gitextensions/pull/4093
[4092]:https://github.com/gitextensions/gitextensions/pull/4092
[4088]:https://github.com/gitextensions/gitextensions/pull/4088
[4087]:https://github.com/gitextensions/gitextensions/pull/4087
[4086]:https://github.com/gitextensions/gitextensions/pull/4086
[4085]:https://github.com/gitextensions/gitextensions/pull/4085
[4084]:https://github.com/gitextensions/gitextensions/pull/4084
[4079]:https://github.com/gitextensions/gitextensions/pull/4079
[4076]:https://github.com/gitextensions/gitextensions/pull/4076
[4075]:https://github.com/gitextensions/gitextensions/pull/4075
[4074]:https://github.com/gitextensions/gitextensions/pull/4074
[4062]:https://github.com/gitextensions/gitextensions/issues/4062
[4057]:https://github.com/gitextensions/gitextensions/issues/4057
[4052]:https://github.com/gitextensions/gitextensions/pull/4052
[4049]:https://github.com/gitextensions/gitextensions/issues/4049
[4031]:https://github.com/gitextensions/gitextensions/issues/4031
[4028]:https://github.com/gitextensions/gitextensions/issues/4028
[4025]:https://github.com/gitextensions/gitextensions/issues/4025
[4024]:https://github.com/gitextensions/gitextensions/issues/4024
[4022]:https://github.com/gitextensions/gitextensions/pull/4022
[4020]:https://github.com/gitextensions/gitextensions/pull/4020
[4019]:https://github.com/gitextensions/gitextensions/pull/4019
[4016]:https://github.com/gitextensions/gitextensions/issues/4016
[4014]:https://github.com/gitextensions/gitextensions/issues/4014
[4012]:https://github.com/gitextensions/gitextensions/issues/4012
[4008]:https://github.com/gitextensions/gitextensions/pull/4008
[4006]:https://github.com/gitextensions/gitextensions/issues/4006
[3999]:https://github.com/gitextensions/gitextensions/issues/3999
[3990]:https://github.com/gitextensions/gitextensions/issues/3990
[3982]:https://github.com/gitextensions/gitextensions/issues/3982
[3970]:https://github.com/gitextensions/gitextensions/issues/3970
[3966]:https://github.com/gitextensions/gitextensions/issues/3966
[3962]:https://github.com/gitextensions/gitextensions/issues/3962
[3959]:https://github.com/gitextensions/gitextensions/issues/3959
[3955]:https://github.com/gitextensions/gitextensions/pull/3955
[3953]:https://github.com/gitextensions/gitextensions/pull/3953
[3948]:https://github.com/gitextensions/gitextensions/issues/3948
[3947]:https://github.com/gitextensions/gitextensions/issues/3947
[3930]:https://github.com/gitextensions/gitextensions/pull/3930
[3921]:https://github.com/gitextensions/gitextensions/pull/3921
[3920]:https://github.com/gitextensions/gitextensions/pull/3920
[3919]:https://github.com/gitextensions/gitextensions/pull/3919
[3915]:https://github.com/gitextensions/gitextensions/issues/3915
[3908]:https://github.com/gitextensions/gitextensions/issues/3908
[3907]:https://github.com/gitextensions/gitextensions/issues/3907
[3900]:https://github.com/gitextensions/gitextensions/pull/3900
[3899]:https://github.com/gitextensions/gitextensions/issues/3899
[3897]:https://github.com/gitextensions/gitextensions/issues/3897
[3892]:https://github.com/gitextensions/gitextensions/issues/3892
[3887]:https://github.com/gitextensions/gitextensions/issues/3887
[3875]:https://github.com/gitextensions/gitextensions/issues/3875
[3867]:https://github.com/gitextensions/gitextensions/issues/3867
[3860]:https://github.com/gitextensions/gitextensions/issues/3860
[3849]:https://github.com/gitextensions/gitextensions/issues/3849
[3842]:https://github.com/gitextensions/gitextensions/issues/3842
[3839]:https://github.com/gitextensions/gitextensions/issues/3839
[3832]:https://github.com/gitextensions/gitextensions/issues/3832
[3822]:https://github.com/gitextensions/gitextensions/issues/3822
[3810]:https://github.com/gitextensions/gitextensions/issues/3810
[3772]:https://github.com/gitextensions/gitextensions/pull/3772
[3760]:https://github.com/gitextensions/gitextensions/issues/3760
[3759]:https://github.com/gitextensions/gitextensions/issues/3759
[3733]:https://github.com/gitextensions/gitextensions/pull/3733
[3730]:https://github.com/gitextensions/gitextensions/issues/3730
[3725]:https://github.com/gitextensions/gitextensions/issues/3725
[3709]:https://github.com/gitextensions/gitextensions/issues/3709
[3652]:https://github.com/gitextensions/gitextensions/issues/3652
[3525]:https://github.com/gitextensions/gitextensions/issues/3525
[3484]:https://github.com/gitextensions/gitextensions/pull/3484
[3161]:https://github.com/gitextensions/gitextensions/issues/3161
[2870]:https://github.com/gitextensions/gitextensions/issues/2870
[2868]:https://github.com/gitextensions/gitextensions/issues/2868
[2839]:https://github.com/gitextensions/gitextensions/issues/2839
[2495]:https://github.com/gitextensions/gitextensions/pull/2495
[1608]:https://github.com/gitextensions/gitextensions/issues/1608
[1605]:https://github.com/gitextensions/gitextensions/issues/1605
[1583]:https://github.com/gitextensions/gitextensions/issues/1583
[1307]:https://github.com/gitextensions/gitextensions/issues/1307

[4351]:https://github.com/gitextensions/gitextensions/pull/4351
[4349]:https://github.com/gitextensions/gitextensions/issues/4349
[4345]:https://github.com/gitextensions/gitextensions/issues/4345
[4344]:https://github.com/gitextensions/gitextensions/pull/4344
[4343]:https://github.com/gitextensions/gitextensions/pull/4343
[4340]:https://github.com/gitextensions/gitextensions/pull/4340
[4331]:https://github.com/gitextensions/gitextensions/pull/4331
[4330]:https://github.com/gitextensions/gitextensions/pull/4330
[4322]:https://github.com/gitextensions/gitextensions/issues/4322
[4321]:https://github.com/gitextensions/gitextensions/pull/4321
[4320]:https://github.com/gitextensions/gitextensions/pull/4320
[4319]:https://github.com/gitextensions/gitextensions/issues/4319
[4318]:https://github.com/gitextensions/gitextensions/pull/4318
[4316]:https://github.com/gitextensions/gitextensions/issues/4316
[4315]:https://github.com/gitextensions/gitextensions/issues/4315
[4301]:https://github.com/gitextensions/gitextensions/issues/4301
[4296]:https://github.com/gitextensions/gitextensions/issues/4296
[4295]:https://github.com/gitextensions/gitextensions/issues/4295
[4293]:https://github.com/gitextensions/gitextensions/pull/4293
[4209]:https://github.com/gitextensions/gitextensions/pull/4209
[4202]:https://github.com/gitextensions/gitextensions/issues/4202
[4058]:https://github.com/gitextensions/gitextensions/issues/4058
[4031]:https://github.com/gitextensions/gitextensions/issues/4031

[4386]:https://github.com/gitextensions/gitextensions/pull/4386
[4374]:https://github.com/gitextensions/gitextensions/issues/4374
[4373]:https://github.com/gitextensions/gitextensions/issues/4373
[4370]:https://github.com/gitextensions/gitextensions/issues/4370
