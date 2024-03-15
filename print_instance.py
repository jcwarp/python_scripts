import re

def print_yaml(config):
  try:
    amq_hostname = re.search('tcp:\/\/(.+?):61616.*$', config['properties']['jms_brokerUrl'] ).group(1)
    cah_pws = re.search('^(.+?),(.+?)$', config['properties']['cah_user_password'])
    cah_pw1 = cah_pws.group(1)
    cah_pw2 = cah_pws.group(2)
    cah_users = re.search('^(.+?),(.+?)$', config['properties']['cah_username'])
    cah_user1 = cah_users.group(1)
    cah_user2 = cah_users.group(2)
    ph_ver = re.search('^.*prime-home-(.+?).tar.bz2$', config['distribution'])
    solr_cfg = re.search('^http:\/\/(.+?):8983\/solr\/(.+?)$', config['properties']['solr_url'])
    solr_hostname = solr_cfg.group(1)
    solr_customer = solr_cfg.group(2)
    taze_hostname = re.search('tcp:\/\/(.+?):61616$', config['properties']['taze_broker_url'] ).group(1)
  except AttributeError:
    print('String parsing failed')


  try:
    print( "# DM instance config\n"
      "'acs_instance_name'                          :", config['clusterId'], "\n"
      "'acs_server_alias'                           :", "\n"
      "'add_jmx_host_address'                       :", config['properties']['jmx_host'], "\n"
      "'amq_hostname'                               :", amq_hostname, "\n"
      "'analytics_provisioning_password1'           :", cah_pw1, "\n"
      "'analytics_provisioning_password2'           :", cah_pw2, "\n"
      "'analytics_provisioning_user1'               :", cah_user1, "\n"
      "'analytics_provisioning_user2'               :", cah_user2, "\n"
      "'auto_plugins'                               :", "\n"
      "'block_mode_password'                        :", config['properties']['block_mode_password'], "\n"
      "'configurator_version'                       :", ph_ver, "\n"
      "'custom_acs_rewrite_cond_and_rules'          :", "\n"
      "'custom_rewrite_cond_and_rules'              :", "\n"
      "'customer_port'                              :", config['nodes'][list(config['nodes'])[0]]['base_port'], "\n"
      "'customer_state'                             :", "\n"
      "'enable_acs_service'                         :", "\n"
      "'db_acs_instance_name'                       :", '_' + config['clusterId'], "\n"
      "'db_hostname'                                :", config['properties']['db_hostname'], "\n"
      "'db_password'                                :", config['properties']['db_password'], "\n"
      "'db_schema'                                  :", config['properties']['db_schema'], "\n"
      "'db_user'                                    :", config['properties']['db_username'], "\n"
      "'enable_acs_service'                         :", "\n"
      "'ext_domain'                                 :", "\n"
      "'jmx_control_role_secret'                    :", config['properties']['jmx_control_role_secret'], "\n"
      "'jmx_monitor_role_secret'                    :", config['properties']['jmx_monitor_role_secret'], "\n"
      "'ldap_enabled'                               :", config.get('properties').get('externalAuthentication_beanName'), "\n"
      "'max_num_sessions'                           :", config['license']['MaxNumberOfSessions'], "\n"
      "'mongodb_list'                               :", config['properties']['clearsight_audit_logMongoUri'], "\n"
      "'newrelic_lic'                               :", config['properties']['newrelic_license_key'], "\n"
      "'oidc_bearer_auth_enabled'                   :", config['properties']['oidc_bearerAuthEnabled'], "\n"
      "'oidc_role_key'                              :", config['properties']['oidc_roleKey'], "\n"
      "'oidc_tenant_id_csv'                         :", config['properties']['oidc_tenantIdCsv'], "\n"
      "'oidc_trusted_issuer_csv'                    :", config['properties']['oidc_trustedIssuerCsv'], "\n"
      "'port_number'                                :", config['nodes'][list(config['nodes'])[0]]['base_port'], "\n"
      "'root_password'                              :", "\n"
      "'safe_mode_password'                         :", config['properties']['safe_mode_password'], "\n"
      "'saml_cp_sso_enable'                         :", config['properties']['saml_cp_sso_enable'], "\n"
      "'saml_cp_sso_key_alias'                      :", config['properties']['saml_cp_sso_key_alias'], "\n"
      "'saml_cp_sso_keystore'                       :", config['properties']['saml_cp_sso_keystore'], "\n"
      "'saml_cp_sso_keystore_passwd'                :", config['properties']['saml_cp_sso_keystore_passwd'], "\n"
      "'saml_cp_sso_privatekey_passwd'              :", config['properties']['saml_cp_sso_privatekey_passwd'], "\n"
      "'saml_sso_callback_url'                      :", config['properties']['saml_sso_callback_url'], "\n"
      "'saml_sso_cp_callback_url'                   :", config['properties']['saml_sso_cp_callback_url'], "\n"
      "'saml_sso_cp_idp_metadata'                   :", config['properties']['saml_sso_cp_idp_metadata'], "\n"
      "'saml_sso_cp_logout_url'                     :", config['properties']['saml_sso_cp_logout_url'], "\n"
      "'saml_sso_cp_max_life_time'                  :", config['properties']['saml_sso_cp_max_life_time'], "\n"
      "'saml_sso_cp_subscriber_code'                :", config['properties']['saml_sso_cp_subscriber_code'], "\n"
      "'saml_sso_cp_userprofile_email_attribute'    :", config['properties']['saml_sso_cp_userprofile_email_attribute'], "\n"
      "'saml_sso_cp_userprofile_fullname_attribute' :", config['properties']['saml_sso_cp_userprofile_fullname_attribute'], "\n"
      "'saml_sso_cp_userprofile_role_attribute'     :", config['properties']['saml_sso_cp_userprofile_role_attribute'], "\n"
      "'saml_sso_enable'                            :", config['properties']['saml_sso_enable'], "\n"
      "'saml_sso_idp_metadata'                      :", config['properties']['saml_sso_idp_metadata'], "\n"
      "'saml_sso_keystore'                          :", config['properties']['saml_sso_keystore'], "\n"
      "'saml_sso_keystore_password'                 :", config['properties']['saml_sso_keystore_passwd'], "\n"
      "'saml_sso_logout_url'                        :", config['properties']['saml_sso_logout_url'], "\n"
      "'saml_sso_privatekey_passwd'                 :", config['properties']['saml_sso_privatekey_passwd'], "\n"
      "'saml_sso_subscriber_code'                   :", config['properties']['saml_sso_subscriber_code'], "\n"
      "'saml_sso_userprofile_domain_attribute'      :", config['properties']['saml_sso_userprofile_domain_attribute'], "\n"
      "'saml_sso_userprofile_email_attribute'       :", config['properties']['saml_sso_userprofile_email_attribute'], "\n"
      "'saml_sso_userprofile_fullname_attribute'    :", config['properties']['saml_sso_userprofile_fullname_attribute'], "\n"
      "'saml_sso_userprofile_role_attribute'        :", config['properties']['saml_sso_userprofile_role_attribute'], "\n"
      "'smartrg_db_password'                        :", config['properties']['db_password'], "\n"
      "'solr_customer'                              :", solr_customer, "\n"
      "'solr_hostname'                              :", solr_hostname, "\n"
      "'system_user_password'                       :", config['properties']['system_user_password'], "\n"
      "'taze_enabled'                               :", config['properties']['taze_enabled'], "\n"
      "'taze_hostname'                              :", taze_hostname, "\n"
      "'trust_store_name'                           :", config['nodes'][list(config['nodes'])[0]]['trust_store_location'], "\n"
      "'cv_home'                                    :", "\n"
      "'acs_nodes'                                  :", config['nodes'], "\n"
      "'overlays'                                   :", config['overlays'], "\n"
    )
  except KeyError as ke:
      print('Key Not Found in Config:', ke)
