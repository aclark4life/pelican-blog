I love collective-recipe-plonesite!
===================================

:date: 2014-06-02 18:15
:tags: Plone, Python

Whenever I answer tech support questions, I usually begin with a clean slate, e.g.::

    $ pip install tmp virtualenv
    $ cd `tmp` 
    $ virtualenv .
    $ bin/pip install zc.buildout
    $ bin/buildout init

Then I edit ``buildout.cfg`` to look like this::

    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-4-3


Then I run Buildout::

    $ bin/buildout

And because my ``.buildout/default.cfg`` file looks like this::

    [buildout]
    eggs-directory = /Users/aclark/Developer/eggs-directory
    download-cache = /Users/aclark/Developer/download-cache
    extends-cache = /Users/aclark/Developer/extends-cache

, the entire process only takes a few seconds (except for when I `run into trouble with setuptools <http://blog.aclark.net/2014/03/19/virtualenv-support-update/>`_. I should probably start doing ``virtualenv --no-setuptools``. Perhaps this can be made default?)

If I'm in the mood to search the source code, I add the following::

    [buildout]
    extends = 
        https://raw.github.com/plock/pins/master/plone-4-3
        https://raw.github.com/plock/pins/master/dev

Then I run Buildout, after which I can easily search in ``parts/omelette``.

Plone site debug
----------------

Anyway, sometimes instead of running Plone through-the-web I want to run a debug prompt instead. All that is required is::

    $ bin/plone debug

However at this point there is no Plone site object in the database. One could easily create a Plone site through-the-web, but why bother when `collective.recipe.plonesite <https://pypi.python.org/pypi/collective.recipe.plonesite>`_ exists::

    [buildout]
    extends = 
        https://raw.github.com/plock/pins/master/plone-4-3
        https://raw.github.com/plock/pins/master/dev
    parts += plonesite

    [plonesite]
    recipe = collective.recipe.plonesite
    instance = plone

After running Buildout, now I can examine the Plone site::

    $ bin/plone debug
    Starting debugger (the name "app" is bound to the top-level Zope object)

    >>> app.Plone.
    Display all 864 possibilities? (y or n)
    app.Plone.COPY(                                                 app.Plone.hasObject__roles__
    app.Plone.COPY__roles__                                         app.Plone.hasProperty(
    app.Plone.Contributors(                                         app.Plone.hasProperty__roles__
    app.Plone.Contributors__roles__                                 app.Plone.has_local_roles(
    app.Plone.CreationDate(                                         app.Plone.has_order_support
    app.Plone.CreationDate__roles__                                 app.Plone.http__etag(
    app.Plone.Creator(                                              app.Plone.http__parseMatchList(
    app.Plone.Creator__roles__                                      app.Plone.http__processMatchHeaders(
    app.Plone.DELETE(                                               app.Plone.http__refreshEtag(
    app.Plone.DELETE__roles__                                       app.Plone.icon
    app.Plone.Date(                                                 app.Plone.icon__roles__
    app.Plone.Date__roles__                                         app.Plone.id
    app.Plone.Description(                                          app.Plone.indexObject(
    app.Plone.Description__roles__                                  app.Plone.invokeFactory(
    app.Plone.EffectiveDate(                                        app.Plone.invokeFactory__roles__
    app.Plone.EffectiveDate__roles__                                app.Plone.isAnObjectManager
    app.Plone.ExpirationDate(                                       app.Plone.isEffective(
    app.Plone.ExpirationDate__roles__                               app.Plone.isEffective__roles__
    app.Plone.Format(                                               app.Plone.isPrincipiaFolderish
    app.Plone.Format__roles__                                       app.Plone.isTopLevelPrincipiaApplicationObject
    app.Plone.HEAD(                                                 app.Plone.items(
    app.Plone.HEAD__roles__                                         app.Plone.items__roles__
    app.Plone.HTTPCache                                             app.Plone.keys(
    app.Plone.Identifier(                                           app.Plone.keys__roles__
    app.Plone.Identifier__roles__                                   app.Plone.language
    app.Plone.LOCK(                                                 app.Plone.listContributors(
    app.Plone.LOCK__roles__                                         app.Plone.listContributors__roles__
    app.Plone.Language(                                             app.Plone.listCreators(
    app.Plone.Language__roles__                                     app.Plone.listCreators__roles__
    app.Plone.MKCOL(                                                app.Plone.listDAVObjects(
    app.Plone.MKCOL_handler(                                        app.Plone.listDAVObjects__roles__
    app.Plone.MOVE(                                                 app.Plone.listFolderContents(
    app.Plone.MOVE__roles__                                         app.Plone.listFolderContents__roles__
    app.Plone.MailHost                                              app.Plone.list_imports(
    app.Plone.ModificationDate(                                     app.Plone.manage(
    app.Plone.ModificationDate__roles__                             app.Plone.manage_CopyContainerAllItems(
    app.Plone.OPTIONS(                                              app.Plone.manage_CopyContainerAllItems__roles__
    app.Plone.OPTIONS__roles__                                      app.Plone.manage_CopyContainerFirstItem(
    app.Plone.PROPFIND(                                             app.Plone.manage_CopyContainerFirstItem__roles__
    app.Plone.PROPFIND__roles__                                     app.Plone.manage_DAVget(
    app.Plone.PROPPATCH(                                            app.Plone.manage_DAVget__roles__
    app.Plone.PROPPATCH__roles__                                    app.Plone.manage_FTPlist(
    app.Plone.PUT(                                                  app.Plone.manage_FTPlist__roles__
    app.Plone.PUT_factory(                                          app.Plone.manage_FTPstat(
    app.Plone.PrincipiaFind(                                        app.Plone.manage_FTPstat__roles__
    app.Plone.PrincipiaFind__roles__                                app.Plone.manage_UndoForm(
    app.Plone.Publisher(                                            app.Plone.manage_UndoForm__roles__
    app.Plone.Publisher__roles__                                    app.Plone.manage__roles__
    app.Plone.RAMCache                                              app.Plone.manage_access(
    app.Plone.REQUEST                                               app.Plone.manage_access__roles__
    app.Plone.ResourceRegistryCache                                 app.Plone.manage_acquiredForm(
    app.Plone.Rights(                                               app.Plone.manage_acquiredForm__roles__
    app.Plone.Rights__roles__                                       app.Plone.manage_acquiredPermissions(
    app.Plone.SQLConnectionIDs(                                     app.Plone.manage_acquiredPermissions__roles__
    app.Plone.SQLConnectionIDs__roles__                             app.Plone.manage_addDTMLDocument(
    app.Plone.SiteRootAdd(                                          app.Plone.manage_addDTMLDocument__roles__
    app.Plone.SiteRootAdd__roles__                                  app.Plone.manage_addDTMLMethod(
    app.Plone.Subject(                                              app.Plone.manage_addDTMLMethod__roles__
    app.Plone.Subject__roles__                                      app.Plone.manage_addDocument(
    app.Plone.TRACE(                                                app.Plone.manage_addDocument__roles__
    app.Plone.TRACE__roles__                                        app.Plone.manage_addFile(
    app.Plone.Title(                                                app.Plone.manage_addFile__roles__
    app.Plone.Title__roles__                                        app.Plone.manage_addFolder(
    app.Plone.Type(                                                 app.Plone.manage_addFolder__roles__
    app.Plone.Type__roles__                                         app.Plone.manage_addImage(
    app.Plone.UNLOCK(                                               app.Plone.manage_addImage__roles__
    app.Plone.UNLOCK__roles__                                       app.Plone.manage_addLocalRoles(
    app.Plone.ZQueryIds(                                            app.Plone.manage_addLocalRoles__roles__
    app.Plone.ZQueryIds__roles__                                    app.Plone.manage_addOrderedFolder(
    app.Plone.ZopeFind(                                             app.Plone.manage_addOrderedFolder__roles__
    app.Plone.ZopeFindAndApply(                                     app.Plone.manage_addPortalFolder(
    app.Plone.ZopeFindAndApply__roles__                             app.Plone.manage_addPortalFolder__roles__
    app.Plone.ZopeFind__roles__                                     app.Plone.manage_addProduct
    app.Plone._ATContentTypes__Add_Document_Permission              app.Plone.manage_addProperty(
    app.Plone._ATContentTypes__Add_Event_Permission                 app.Plone.manage_addProperty__roles__
    app.Plone._ATContentTypes__Add_File_Permission                  app.Plone.manage_addSiteRoot(
    app.Plone._ATContentTypes__Add_Folder_Permission                app.Plone.manage_addSiteRootForm(
    app.Plone._ATContentTypes__Add_Image_Permission                 app.Plone.manage_addSiteRootForm__roles__
    app.Plone._ATContentTypes__Add_Link_Permission                  app.Plone.manage_addSiteRoot__roles__
    app.Plone._ATContentTypes__Add_News_Item_Permission             app.Plone.manage_addUserFolder(
    app.Plone._Access_arbitrary_user_session_data_Permission        app.Plone.manage_addUserFolder__roles__
    app.Plone._Access_contents_information_Permission               app.Plone.manage_afterAdd(
    app.Plone._Access_inactive_portal_content_Permission            app.Plone.manage_afterAdd__roles__
    app.Plone._Access_session_data_Permission                       app.Plone.manage_afterClone(
    app.Plone._Add_portal_content_Permission                        app.Plone.manage_afterClone__roles__
    app.Plone._Add_portal_events_Permission                         app.Plone.manage_beforeDelete(
    app.Plone._Add_portal_folders_Permission                        app.Plone.manage_beforeDelete__roles__
    app.Plone._Add_portal_member_Permission                         app.Plone.manage_changeOwnershipType(
    app.Plone._Allow_sendto_Permission                              app.Plone.manage_changeOwnershipType__roles__
    app.Plone._CMFEditions__Access_previous_versions_Permission     app.Plone.manage_changePermissions(
    app.Plone._CMFEditions__Apply_version_control_Permission        app.Plone.manage_changePermissions__roles__
    app.Plone._CMFEditions__Checkout_to_location_Permission         app.Plone.manage_changeProperties(
    app.Plone._CMFEditions__Revert_to_previous_versions_Permission  app.Plone.manage_changeProperties__roles__
    app.Plone._CMFEditions__Save_new_version_Permission             app.Plone.manage_changePropertyTypes(
    app.Plone._Change_local_roles_Permission                        app.Plone.manage_changePropertyTypes__roles__
    app.Plone._Change_portal_events_Permission                      app.Plone.manage_clone(
    app.Plone._Content_rules__Manage_rules_Permission               app.Plone.manage_clone__roles__
    app.Plone._Copy_or_Move_Permission                              app.Plone.manage_copyObjects(
    app.Plone._DefaultDublinCoreImpl__CEILING_DATE                  app.Plone.manage_copyObjects__roles__
    app.Plone._DefaultDublinCoreImpl__FLOOR_DATE                    app.Plone.manage_copyright(
    app.Plone._Delete_objects_Permission                            app.Plone.manage_copyright__roles__
    app.Plone._FTP_access_Permission                                app.Plone.manage_cutObjects(
    app.Plone._List_folder_contents_Permission                      app.Plone.manage_cutObjects__roles__
    app.Plone._List_portal_members_Permission                       app.Plone.manage_defined_roles(
    app.Plone._List_undoable_changes_Permission                     app.Plone.manage_defined_roles__roles__
    app.Plone._Mail_forgotten_password_Permission                   app.Plone.manage_delLocalRoles(
    app.Plone._Manage_properties_Permission                         app.Plone.manage_delLocalRoles__roles__
    app.Plone._Modify_portal_content_Permission                     app.Plone.manage_delObjects(
    app.Plone._Modify_view_template_Permission                      app.Plone.manage_delObjects__roles__
    app.Plone._Portlets__Manage_own_portlets_Permission             app.Plone.manage_delProperties(
    app.Plone._Portlets__Manage_portlets_Permission                 app.Plone.manage_delProperties__roles__
    app.Plone._Portlets__View_dashboard_Permission                  app.Plone.manage_editLocalRoles(
    app.Plone._Reply_to_item_Permission                             app.Plone.manage_editLocalRoles__roles__
    app.Plone._Request_review_Permission                            app.Plone.manage_editMetadata(
    app.Plone._Review_comments_Permission                           app.Plone.manage_editMetadata__roles__
    app.Plone._Review_portal_content_Permission                     app.Plone.manage_editProperties(
    app.Plone._Search_ZCatalog_Permission                           app.Plone.manage_editProperties__roles__
    app.Plone._Set_own_password_Permission                          app.Plone.manage_editRoles(
    app.Plone._Set_own_properties_Permission                        app.Plone.manage_editRoles__roles__
    app.Plone._Undo_changes_Permission                              app.Plone.manage_editedDialog(
    app.Plone._Use_Database_Methods_Permission                      app.Plone.manage_editedDialog__roles__
    app.Plone._Use_external_editor_Permission                       app.Plone.manage_exportObject(
    app.Plone._Use_mailhost_services_Permission                     app.Plone.manage_exportObject__roles__
    app.Plone._Use_version_control_Permission                       app.Plone.manage_findAdv(
    app.Plone._View_Groups_Permission                               app.Plone.manage_findAdv__roles__
    app.Plone._View_History_Permission                              app.Plone.manage_findForm(
    app.Plone._View_Permission                                      app.Plone.manage_findForm__roles__
    app.Plone._View_management_screens_Permission                   app.Plone.manage_findFrame(
    app.Plone._WebDAV_Lock_items_Permission                         app.Plone.manage_findFrame__roles__
    app.Plone._WebDAV_Unlock_items_Permission                       app.Plone.manage_findResult(
    app.Plone._WebDAV_access_Permission                             app.Plone.manage_findResult__roles__
    app.Plone.__ZCacheManager_ids__                                 app.Plone.manage_fixupOwnershipAfterAdd(
    app.Plone.__ac_local_roles__                                    app.Plone.manage_fixupOwnershipAfterAdd__roles__
    app.Plone.__ac_permissions__                                    app.Plone.manage_form_title(
    app.Plone.__ac_roles__                                          app.Plone.manage_form_title__roles__
    app.Plone.__allow_access_to_unprotected_subobjects__            app.Plone.manage_getPermissionMapping(
    app.Plone.__allow_groups__(                                     app.Plone.manage_getPermissionMapping__roles__
    app.Plone.__before_publishing_traverse__(                       app.Plone.manage_getUserRolesAndPermissions(
    app.Plone.__before_traverse__                                   app.Plone.manage_getUserRolesAndPermissions__roles__
    app.Plone.__browser_default__(                                  app.Plone.manage_hasId(
    app.Plone.__call__(                                             app.Plone.manage_hasId__roles__
    app.Plone.__call____roles__                                     app.Plone.manage_importExportForm(
    app.Plone.__class__(                                            app.Plone.manage_importExportForm__roles__
    app.Plone.__class_init__(                                       app.Plone.manage_importObject(
    app.Plone.__contains__(                                         app.Plone.manage_importObject__roles__
    app.Plone.__dav_collection__                                    app.Plone.manage_index_main(
    app.Plone.__dav_resource__                                      app.Plone.manage_index_main__roles__
    app.Plone.__delattr__(                                          app.Plone.manage_listLocalRoles(
    app.Plone.__delitem__(                                          app.Plone.manage_listLocalRoles__roles__
    app.Plone.__dict__                                              app.Plone.manage_main(
    app.Plone.__doc__                                               app.Plone.manage_main__roles__
    app.Plone.__error_log__                                         app.Plone.manage_menu(
    app.Plone.__format__(                                           app.Plone.manage_menu__roles__
    app.Plone.__getattr__(                                          app.Plone.manage_metadata(
    app.Plone.__getattribute__(                                     app.Plone.manage_metadata__roles__
    app.Plone.__getitem__(                                          app.Plone.manage_move_objects_down(
    app.Plone.__getstate__(                                         app.Plone.manage_move_objects_down__roles__
    app.Plone.__hash__(                                             app.Plone.manage_move_objects_to_bottom(
    app.Plone.__http_methods__                                      app.Plone.manage_move_objects_to_bottom__roles__
    app.Plone.__implemented__(                                      app.Plone.manage_move_objects_to_top(
    app.Plone.__init__(                                             app.Plone.manage_move_objects_to_top__roles__
    app.Plone.__iter__(                                             app.Plone.manage_move_objects_up(
    app.Plone.__len__(                                              app.Plone.manage_move_objects_up__roles__
    app.Plone.__module__                                            app.Plone.manage_options
    app.Plone.__name__                                              app.Plone.manage_owner(
    app.Plone.__new__(                                              app.Plone.manage_owner__roles__
    app.Plone.__nonzero__(                                          app.Plone.manage_page_footer(
    app.Plone.__of__(                                               app.Plone.manage_page_footer__roles__
    app.Plone.__old_manage_FTPlist(                                 app.Plone.manage_page_header(
    app.Plone.__propsets__                                          app.Plone.manage_page_header__roles__
    app.Plone.__providedBy__(                                       app.Plone.manage_page_style.css(
    app.Plone.__provides__(                                         app.Plone.manage_page_style.css__roles__
    app.Plone.__reduce__(                                           app.Plone.manage_pasteObjects(
    app.Plone.__reduce_ex__(                                        app.Plone.manage_pasteObjects__roles__
    app.Plone.__replaceable__                                       app.Plone.manage_permission(
    app.Plone.__repr__(                                             app.Plone.manage_permissionForm(
    app.Plone.__roles__                                             app.Plone.manage_permissionForm__roles__
    app.Plone.__setattr__(                                          app.Plone.manage_permission__roles__
    app.Plone.__setitem__(                                          app.Plone.manage_propertiesForm(
    app.Plone.__setstate__(                                         app.Plone.manage_propertiesForm__roles__
    app.Plone.__sizeof__(                                           app.Plone.manage_propertyTypeForm(
    app.Plone.__str__(                                              app.Plone.manage_propertyTypeForm__roles__
    app.Plone.__subclasshook__(                                     app.Plone.manage_renameForm(
    app.Plone.__weakref__                                           app.Plone.manage_renameForm__roles__
    app.Plone._addRole(                                             app.Plone.manage_renameObject(
    app.Plone._at_fti_meta_type                                     app.Plone.manage_renameObject__roles__
    app.Plone._canCopy(                                             app.Plone.manage_renameObjects(
    app.Plone._checkId(                                             app.Plone.manage_renameObjects__roles__
    app.Plone._components                                           app.Plone.manage_reportUserPermissions(
    app.Plone._datify(                                              app.Plone.manage_reportUserPermissions__roles__
    app.Plone._datify__roles__                                      app.Plone.manage_role(
    app.Plone._default_sort_key                                     app.Plone.manage_roleForm(
    app.Plone._default_sort_reverse                                 app.Plone.manage_roleForm__roles__
    app.Plone._delOb(                                               app.Plone.manage_role__roles__
    app.Plone._delObject(                                           app.Plone.manage_setLocalRoles(
    app.Plone._delPropValue(                                        app.Plone.manage_setLocalRoles__roles__
    app.Plone._delProperty(                                         app.Plone.manage_setPermissionMapping(
    app.Plone._delRoles(                                            app.Plone.manage_setPermissionMapping__roles__
    app.Plone._deleteOwnershipAfterAdd(                             app.Plone.manage_set_default_sorting(
    app.Plone._editMetadata(                                        app.Plone.manage_set_default_sorting__roles__
    app.Plone._editMetadata__roles__                                app.Plone.manage_tabs(
    app.Plone._filteredItems(                                       app.Plone.manage_tabs__roles__
    app.Plone._getCopy(                                             app.Plone.manage_takeOwnership(
    app.Plone._getImportPaths(                                      app.Plone.manage_takeOwnership__roles__
    app.Plone._getOb(                                               app.Plone.manage_top_frame(
    app.Plone._getPortalTypeName(                                   app.Plone.manage_top_frame__roles__
    app.Plone._getUNIQUE(                                           app.Plone.manage_undo_transactions(
    app.Plone._get_id(                                              app.Plone.manage_undo_transactions__roles__
    app.Plone._get_request_var_or_attr(                             app.Plone.manage_workspace(
    app.Plone._has_user_defined_role(                               app.Plone.manage_workspace__roles__
    app.Plone._importObjectFromFile(                                app.Plone.manage_zmi_logout(
    app.Plone._isBeingUsedAsAMethod(                                app.Plone.manage_zmi_logout__roles__
    app.Plone._manage_editedDialog(                                 app.Plone.manage_zmi_prefs(
    app.Plone._normal_manage_access(                                app.Plone.manage_zmi_prefs__roles__
    app.Plone._notifyOfCopyTo(                                      app.Plone.management_page_charset
    app.Plone._objects                                              app.Plone.meta_type
    app.Plone._old_filtered_manage_options(                         app.Plone.meta_types
    app.Plone._owner                                                app.Plone.mimetypes_registry(
    app.Plone._p_activate(                                          app.Plone.modification_date
    app.Plone._p_changed                                            app.Plone.modified(
    app.Plone._p_deactivate(                                        app.Plone.modified__roles__
    app.Plone._p_delattr(                                           app.Plone.moveObject(
    app.Plone._p_estimated_size                                     app.Plone.moveObjectToPosition(
    app.Plone._p_getattr(                                           app.Plone.moveObjectToPosition__roles__
    app.Plone._p_invalidate(                                        app.Plone.moveObject__roles__
    app.Plone._p_jar                                                app.Plone.moveObjectsByDelta(
    app.Plone._p_mtime                                              app.Plone.moveObjectsByDelta__roles__
    app.Plone._p_oid                                                app.Plone.moveObjectsDown(
    app.Plone._p_serial                                             app.Plone.moveObjectsDown__roles__
    app.Plone._p_setattr(                                           app.Plone.moveObjectsToBottom(
    app.Plone._p_state                                              app.Plone.moveObjectsToBottom__roles__
    app.Plone._plone_app_collection__Add_Collection_Permission      app.Plone.moveObjectsToTop(
    app.Plone._postCopy(                                            app.Plone.moveObjectsToTop__roles__
    app.Plone._properties                                           app.Plone.moveObjectsUp(
    app.Plone._propertyMap(                                         app.Plone.moveObjectsUp__roles__
    app.Plone._reserved_names                                       app.Plone.notifyModified(
    app.Plone._setId(                                               app.Plone.notifyModified__roles__
    app.Plone._setOb(                                               app.Plone.objectIds(
    app.Plone._setObject(                                           app.Plone.objectIds__roles__
    app.Plone._setPortalTypeName(                                   app.Plone.objectIds_d(
    app.Plone._setPropValue(                                        app.Plone.objectIds_d__roles__
    app.Plone._setProperty(                                         app.Plone.objectItems(
    app.Plone._setRoles(                                            app.Plone.objectItems__roles__
    app.Plone._subobject_permissions(                               app.Plone.objectItems_d(
    app.Plone._updateProperty(                                      app.Plone.objectItems_d__roles__
    app.Plone._verifyObjectPaste(                                   app.Plone.objectMap(
    app.Plone._wrapperCheck(                                        app.Plone.objectMap_d(
    app.Plone.absolute_url(                                         app.Plone.objectMap_d__roles__
    app.Plone.absolute_url__roles__                                 app.Plone.objectValues(
    app.Plone.absolute_url_path(                                    app.Plone.objectValues__roles__
    app.Plone.absolute_url_path__roles__                            app.Plone.objectValues_d(
    app.Plone.ac_inherited_permissions(                             app.Plone.objectValues_d__roles__
    app.Plone.ac_inherited_permissions__roles__                     app.Plone.opaqueIds(
    app.Plone.access_debug_info(                                    app.Plone.opaqueIds__roles__
    app.Plone.access_debug_info__roles__                            app.Plone.opaqueItems(
    app.Plone.aclAChecked                                           app.Plone.opaqueItems__roles__
    app.Plone.aclEChecked                                           app.Plone.opaqueValues(
    app.Plone.aclPChecked                                           app.Plone.opaqueValues__roles__
    app.Plone.acl_users(                                            app.Plone.orderObjects(
    app.Plone.acquiredRolesAreUsedBy(                               app.Plone.orderObjects__roles__
    app.Plone.acquiredRolesAreUsedBy__roles__                       app.Plone.owner_info(
    app.Plone.addCreator(                                           app.Plone.owner_info__roles__
    app.Plone.addCreator__roles__                                   app.Plone.permission_settings(
    app.Plone.addDTMLDocument(                                      app.Plone.permission_settings__roles__
    app.Plone.addDTMLDocument__roles__                              app.Plone.permissionsOfRole(
    app.Plone.addDTMLMethod(                                        app.Plone.permissionsOfRole__roles__
    app.Plone.addDTMLMethod__roles__                                app.Plone.plone_utils
    app.Plone.aliases                                               app.Plone.portal_actionicons(
    app.Plone.all_meta_types(                                       app.Plone.portal_actions
    app.Plone.allowedContentTypes(                                  app.Plone.portal_archivist
    app.Plone.allowedContentTypes__roles__                          app.Plone.portal_atct
    app.Plone.analyseDocumentation(                                 app.Plone.portal_calendar
    app.Plone.analyseDocumentation__roles__                         app.Plone.portal_catalog(
    app.Plone.archetype_tool                                        app.Plone.portal_controlpanel
    app.Plone.availableLanguages(                                   app.Plone.portal_css
    app.Plone.availableLanguages__roles__                           app.Plone.portal_diff
    app.Plone.bobobase_modification_time(                           app.Plone.portal_discussion
    app.Plone.caching_policy_manager                                app.Plone.portal_factory(
    app.Plone.canSetDefaultPage(                                    app.Plone.portal_form_controller(
    app.Plone.canSetDefaultPage__roles__                            app.Plone.portal_groupdata
    app.Plone.canSetLayout(                                         app.Plone.portal_groups
    app.Plone.canSetLayout__roles__                                 app.Plone.portal_historiesstorage
    app.Plone.cb_dataItems(                                         app.Plone.portal_historyidhandler
    app.Plone.cb_dataValid(                                         app.Plone.portal_interface
    app.Plone.cb_isCopyable(                                        app.Plone.portal_javascripts
    app.Plone.cb_isMoveable(                                        app.Plone.portal_languages(
    app.Plone.cb_userHasCopyOrMovePermission(                       app.Plone.portal_memberdata
    app.Plone.changeOwnership(                                      app.Plone.portal_membership
    app.Plone.changeOwnership__roles__                              app.Plone.portal_metadata
    app.Plone.changeSkin(                                           app.Plone.portal_migration
    app.Plone.changeSkin__roles__                                   app.Plone.portal_modifier
    app.Plone.checkIdAvailable(                                     app.Plone.portal_password_reset
    app.Plone.checkIdAvailable__roles__                             app.Plone.portal_properties
    app.Plone.clearCurrentSkin(                                     app.Plone.portal_purgepolicy
    app.Plone.clearCurrentSkin__roles__                             app.Plone.portal_quickinstaller
    app.Plone.contentIds(                                           app.Plone.portal_referencefactories
    app.Plone.contentIds__roles__                                   app.Plone.portal_registration
    app.Plone.contentItems(                                         app.Plone.portal_registry
    app.Plone.contentItems__roles__                                 app.Plone.portal_repository
    app.Plone.contentValues(                                        app.Plone.portal_setup
    app.Plone.contentValues__roles__                                app.Plone.portal_skins
    app.Plone.content_type(                                         app.Plone.portal_tinymce
    app.Plone.content_type_registry                                 app.Plone.portal_transforms(
    app.Plone.contributors                                          app.Plone.portal_type
    app.Plone.created(                                              app.Plone.portal_types
    app.Plone.created__roles__                                      app.Plone.portal_uidannotation(
    app.Plone.creation_date                                         app.Plone.portal_uidgenerator(
    app.Plone.creators                                              app.Plone.portal_uidhandler
    app.Plone.dav__init(                                            app.Plone.portal_undo
    app.Plone.dav__simpleifhandler(                                 app.Plone.portal_url(
    app.Plone.dav__validate(                                        app.Plone.portal_view_customizations
    app.Plone.decodeFolderFilter(                                   app.Plone.portal_workflow
    app.Plone.decodeFolderFilter__roles__                           app.Plone.possible_permissions(
    app.Plone.defaultView(                                          app.Plone.propdict(
    app.Plone.defaultView__roles__                                  app.Plone.propdict__roles__
    app.Plone.default_view                                          app.Plone.propertyDescription(
    app.Plone.description                                           app.Plone.propertyDescription__roles__
    app.Plone.edit(                                                 app.Plone.propertyIds(
    app.Plone.editMetadata(                                         app.Plone.propertyIds__roles__
    app.Plone.editMetadata__roles__                                 app.Plone.propertyItems(
    app.Plone.edit__roles__                                         app.Plone.propertyItems__roles__
    app.Plone.effective(                                            app.Plone.propertyLabel(
    app.Plone.effective__roles__                                    app.Plone.propertyLabel__roles__
    app.Plone.effective_date                                        app.Plone.propertyMap(
    app.Plone.email_charset                                         app.Plone.propertyMap__roles__
    app.Plone.email_from_address                                    app.Plone.propertyValues(
    app.Plone.email_from_name                                       app.Plone.propertyValues__roles__
    app.Plone.enable_permalink                                      app.Plone.propertysheets
    app.Plone.encodeFolderFilter(                                   app.Plone.raise_standardErrorMessage(
    app.Plone.encodeFolderFilter__roles__                           app.Plone.reference_catalog(
    app.Plone.error_log                                             app.Plone.reindexObject(
    app.Plone.expiration_date                                       app.Plone.reindexObjectSecurity(
    app.Plone.expires(                                              app.Plone.restrictedTraverse(
    app.Plone.expires__roles__                                      app.Plone.restrictedTraverse__roles__
    app.Plone.externalEditLink_(                                    app.Plone.rights
    app.Plone.externalEdit_                                         app.Plone.rolesOfPermission(
    app.Plone.filtered_manage_options(                              app.Plone.rolesOfPermission__roles__
    app.Plone.filtered_manage_options__roles__                      app.Plone.selectable_views
    app.Plone.filtered_meta_types(                                  app.Plone.selectedRoles
    app.Plone.folderlistingFolderContents(                          app.Plone.setContributors(
    app.Plone.folderlistingFolderContents__roles__                  app.Plone.setContributors__roles__
    app.Plone.format                                                app.Plone.setCreators(
    app.Plone.get(                                                  app.Plone.setCreators__roles__
    app.Plone.getActionInfo(                                        app.Plone.setDefaultPage(
    app.Plone.getActionInfo__roles__                                app.Plone.setDefaultPage__roles__
    app.Plone.getAttribute(                                         app.Plone.setDefaultSorting(
    app.Plone.getAttributeNode(                                     app.Plone.setDefaultSorting__roles__
    app.Plone.getAttributeNode__roles__                             app.Plone.setDescription(
    app.Plone.getAttribute__roles__                                 app.Plone.setDescription__roles__
    app.Plone.getAttributes(                                        app.Plone.setEffectiveDate(
    app.Plone.getAttributes__roles__                                app.Plone.setEffectiveDate__roles__
    app.Plone.getAvailableLayouts(                                  app.Plone.setExpirationDate(
    app.Plone.getAvailableLayouts__roles__                          app.Plone.setExpirationDate__roles__
    app.Plone.getCMFObjectsSubsetIds(                               app.Plone.setFormat(
    app.Plone.getChildNodes(                                        app.Plone.setFormat__roles__
    app.Plone.getChildNodes__roles__                                app.Plone.setLanguage(
    app.Plone.getCurrentSkinName(                                   app.Plone.setLanguage__roles__
    app.Plone.getCurrentSkinName__roles__                           app.Plone.setLayout(
    app.Plone.getDefaultLayout(                                     app.Plone.setLayout__roles__
    app.Plone.getDefaultLayout__roles__                             app.Plone.setModificationDate(
    app.Plone.getDefaultPage(                                       app.Plone.setModificationDate__roles__
    app.Plone.getDefaultPage__roles__                               app.Plone.setRights(
    app.Plone.getDefaultSorting(                                    app.Plone.setRights__roles__
    app.Plone.getDefaultSorting__roles__                            app.Plone.setSiteManager(
    app.Plone.getElementsByTagName(                                 app.Plone.setSiteManager__roles__
    app.Plone.getElementsByTagName__roles__                         app.Plone.setSubject(
    app.Plone.getFirstChild(                                        app.Plone.setSubject__roles__
    app.Plone.getFirstChild__roles__                                app.Plone.setTitle(
    app.Plone.getIcon(                                              app.Plone.setTitle__roles__
    app.Plone.getIconURL(                                           app.Plone.setupCurrentSkin(
    app.Plone.getIconURL__roles__                                   app.Plone.setupCurrentSkin__roles__
    app.Plone.getIcon__roles__                                      app.Plone.showDocumentation(
    app.Plone.getId(                                                app.Plone.showDocumentation__roles__
    app.Plone.getId__roles__                                        app.Plone.smallRolesWidget
    app.Plone.getIdsSubset(                                         app.Plone.subject
    app.Plone.getIdsSubset__roles__                                 app.Plone.superValues(
    app.Plone.getLastChild(                                         app.Plone.superValues__roles__
    app.Plone.getLastChild__roles__                                 app.Plone.suppl_views
    app.Plone.getLayout(                                            app.Plone.tabs_path_default(
    app.Plone.getLayout__roles__                                    app.Plone.tabs_path_info(
    app.Plone.getMetadataHeaders(                                   app.Plone.this(
    app.Plone.getMetadataHeaders__roles__                           app.Plone.title
    app.Plone.getNextSibling(                                       app.Plone.title_and_id(
    app.Plone.getNextSibling__roles__                               app.Plone.title_or_id(
    app.Plone.getNodeName(                                          app.Plone.tpURL(
    app.Plone.getNodeName__roles__                                  app.Plone.tpValues(
    app.Plone.getNodeType(                                          app.Plone.tpValues__roles__
    app.Plone.getNodeValue(                                         app.Plone.translation_service
    app.Plone.getNodeValue__roles__                                 app.Plone.uid_catalog(
    app.Plone.getObjectPosition(                                    app.Plone.undoable_transactions(
    app.Plone.getObjectPosition__roles__                            app.Plone.undoable_transactions__roles__
    app.Plone.getOwner(                                             app.Plone.unindexObject(
    app.Plone.getOwnerDocument(                                     app.Plone.unrestrictedTraverse(
    app.Plone.getOwnerDocument__roles__                             app.Plone.unrestrictedTraverse__roles__
    app.Plone.getOwnerTuple(                                        app.Plone.userCanTakeOwnership(
    app.Plone.getOwnerTuple__roles__                                app.Plone.userdefined_roles(
    app.Plone.getOwner__roles__                                     app.Plone.userdefined_roles__roles__
    app.Plone.getParentNode(                                        app.Plone.users_with_local_role(
    app.Plone.getParentNode__roles__                                app.Plone.validClipData(
    app.Plone.getPhysicalPath(                                      app.Plone.validRoles(
    app.Plone.getPhysicalPath__roles__                              app.Plone.valid_property_id(
    app.Plone.getPhysicalRoot(                                      app.Plone.valid_property_id__roles__
    app.Plone.getPhysicalRoot__roles__                              app.Plone.valid_roles(
    app.Plone.getPortalTypeName(                                    app.Plone.validate_email
    app.Plone.getPortalTypeName__roles__                            app.Plone.validate_roles(
    app.Plone.getPreviousSibling(                                   app.Plone.values(
    app.Plone.getPreviousSibling__roles__                           app.Plone.values__roles__
    app.Plone.getProperty(                                          app.Plone.view(
    app.Plone.getPropertyType(                                      app.Plone.virtual_url_path(
    app.Plone.getPropertyType__roles__                              app.Plone.virtual_url_path__roles__
    app.Plone.getProperty__roles__                                  app.Plone.wl_clearLocks(
    app.Plone.getSiteManager(                                       app.Plone.wl_clearLocks__roles__
    app.Plone.getSiteManager__roles__                               app.Plone.wl_delLock(
    app.Plone.getSkin(                                              app.Plone.wl_delLock__roles__
    app.Plone.getSkinNameFromRequest(                               app.Plone.wl_getLock(
    app.Plone.getSkinNameFromRequest__roles__                       app.Plone.wl_getLock__roles__
    app.Plone.getSkin__roles__                                      app.Plone.wl_hasLock(
    app.Plone.getSkinsFolderName(                                   app.Plone.wl_isLocked(
    app.Plone.getSkinsFolderName__roles__                           app.Plone.wl_isLockedByUser__roles__
    app.Plone.getTagName(                                           app.Plone.wl_isLocked__roles__
    app.Plone.getTagName__roles__                                   app.Plone.wl_lockItems(
    app.Plone.getTypeInfo(                                          app.Plone.wl_lockItems__roles__
    app.Plone.getTypeInfo__roles__                                  app.Plone.wl_lockTokens(
    app.Plone.getWrappedOwner(                                      app.Plone.wl_lockTokens__roles__
    app.Plone.getWrappedOwner__roles__                              app.Plone.wl_lockValues(
    app.Plone.get__roles__                                          app.Plone.wl_lockValues__roles__
    app.Plone.get_local_roles(                                      app.Plone.wl_lockmapping(
    app.Plone.get_local_roles_for_userid(                           app.Plone.wl_lockmapping__roles__
    app.Plone.get_valid_userids(                                    app.Plone.wl_setLock(
    app.Plone.hasChildNodes(                                        app.Plone.wl_setLock__roles__
    app.Plone.hasChildNodes__roles__                                app.Plone.zope_quick_start(
    app.Plone.hasObject(                                            app.Plone.zope_quick_start__roles__

(*You should probably* `hire me <http://aclark.net>`_ *or* `follow me on Twitter <http://twitter.com/aclark4life>`_ *or both*.)
