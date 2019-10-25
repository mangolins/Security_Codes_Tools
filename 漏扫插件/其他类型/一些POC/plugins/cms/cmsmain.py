#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: cms漏洞库
referer: unknow
author: Lucifer
description: 包含所有cms漏洞类型，封装成一个模块
'''

#泛微
from .weaver_oa.weaver_oa_download_sqli import weaver_oa_download_sqli_BaseVerify
from .weaver_oa.weaver_oa_db_disclosure import weaver_oa_db_disclosure_BaseVerify
from .weaver_oa.weaver_oa_filedownload import weaver_oa_filedownload_BaseVerify

#phpok vulns
from .phpok.phpok_res_action_control_filedownload import phpok_res_action_control_filedownload_BaseVerify
from .phpok.phpok_api_param_sqli import phpok_api_param_sqli_BaseVerify
from .phpok.phpok_remote_image_getshell import phpok_remote_image_getshell_BaseVerify

#typecho vuls
from .typecho.typecho_install_code_exec import typecho_install_code_exec_BaseVerify

#foosun vuls
from .foosun.foosun_City_ajax_sqli import foosun_City_ajax_sqli_BaseVerify

#autoset vuls
from .autoset.autoset_phpmyadmin_unauth import autoset_phpmyadmin_unauth_BaseVerify

#phpstudy vuls
from .phpstudy.phpstudy_probe import phpstudy_probe_BaseVerify
from .phpstudy.phpstudy_phpmyadmin_defaultpwd import phpstudy_phpmyadmin_defaultpwd_BaseVerify

#Hishop vulns
from .Hishop.hishop_productlist_sqli import hishop_productlist_sqli_BaseVerify

#SiteEngine vulns
from .siteengine.siteengine_comments_module_sqli import siteengine_comments_module_sqli_BaseVerify

#zfsoft vulns
from .zfsoft.zfsoft_service_stryhm_sqli import zfsoft_service_stryhm_sqli_BaseVerify
from .zfsoft.zfsoft_database_control import zfsoft_database_control_BaseVerify
from .zfsoft.zfsoft_default3_bruteforce import zfsoft_default3_bruteforce_BaseVerify

#ecshop vulns
from .ecshop.ecshop_uc_code_sqli import ecshop_uc_code_sqli_BaseVerify
from .ecshop.ecshop_flow_orderid_sqli import ecshop_flow_orderid_sqli_BaseVerify

#discuz! vulns
from .discuz.discuz_forum_message_ssrf import discuz_forum_message_ssrf_BaseVerify
from .discuz.discuz_focus_flashxss import discuz_focus_flashxss_BaseVerify
from .discuz.discuz_x25_path_disclosure import discuz_x25_path_disclosure_BaseVerify
from .discuz.discuz_plugin_ques_sqli import discuz_plugin_ques_sqli_BaseVerify

#亿邮 vulns
from .eyou.eyou_weakpass import eyou_weakpass_BaseVerify
from .eyou.eyou_admin_id_sqli import eyou_admin_id_sqli_BaseVerify
from .eyou.eyou_resetpw import eyou_resetpw_BaseVerify
from .eyou.eyou_user_kw_sqli import eyou_user_kw_sqli_BaseVerify

#金蝶 vulns
from .kingdee.kingdee_filedownload import kingdee_filedownload_BaseVerify
from .kingdee.kingdee_resin_dir_path_disclosure import kingdee_resin_dir_path_disclosure_BaseVerify
from .kingdee.kingdee_conf_disclosure import kingdee_conf_disclosure_BaseVerify
from .kingdee.kingdee_logoImgServlet_fileread import kingdee_logoImgServlet_fileread_BaseVerify

#乐语 vulns
from .looyu.looyu_down_filedownload import looyu_down_filedownload_BaseVerify

#smartoa vulns
from .smartoa.smartoa_multi_filedownload import smartoa_multi_filedownload_BaseVerify

#URP vulns
from .urp.urp_query import urp_query_BaseVerify
from .urp.urp_query2 import urp_query2_BaseVerify
from .urp.urp_ReadJavaScriptServlet_fileread import urp_ReadJavaScriptServlet_fileread_BaseVerify

#PKPMBS vulns
from .PKPMBS.pkpmbs_guestbook_sqli import pkpmbs_guestbook_sqli_BaseVerify
from .PKPMBS.pkpmbs_addresslist_keyword_sqli import pkpmbs_addresslist_keyword_sqli_BaseVerify
from .PKPMBS.pkpmbs_MsgList_sqli import pkpmbs_MsgList_sqli_BaseVerify

#帝友 vulns
from .diyou.dyp2p_latesindex_sqli import dyp2p_latesindex_sqli_BaseVerify
from .diyou.dyp2p_url_fileread import dyp2p_url_fileread_BaseVerify

#爱琴斯 vulns
from .iGenus.igenus_code_exec import igenus_code_exec_BaseVerify
from .iGenus.igenus_login_Lang_fileread import igenus_login_Lang_fileread_BaseVerify
from .iGenus.igenus_syslogin_Lang_fileread import igenus_syslogin_Lang_fileread_BaseVerify

#live800 vulns
from .live800.live800_downlog_filedownload import live800_downlog_filedownload_BaseVerify
from .live800.live800_loginAction_sqli import live800_loginAction_sqli_BaseVerify
from .live800.live800_sta_export_sqli import live800_sta_export_sqli_BaseVerify
from .live800.live800_services_xxe import live800_services_xxe_BaseVerify

#thinkphp vulns
from .thinkphp.onethink_category_sqli import onethink_category_sqli_BaseVerify
from .thinkphp.thinkphp_code_exec import thinkphp_code_exec_BaseVerify

#汇思 vulns
from .wizbank.wizbank_download_filedownload import wizbank_download_filedownload_BaseVerify
from .wizbank.wizbank_usr_id_sqli import wizbank_usr_id_sqli_BaseVerify

#汇文 vulns
from .libsys.libsys_ajax_asyn_link_old_fileread import libsys_ajax_asyn_link_old_fileread_BaseVerify
from .libsys.libsys_ajax_asyn_link_fileread import libsys_ajax_asyn_link_fileread_BaseVerify
from .libsys.libsys_ajax_get_file_fileread import libsys_ajax_get_file_fileread_BaseVerify

#通元内容管理系统 vulns
from .gpower.gpower_users_disclosure import gpower_users_disclosure_BaseVerify

#metinfo cms vulns
from .metinfo.metinfo_getpassword_sqli import metinfo_getpassword_sqli_BaseVerify
from .metinfo.metinfo_login_check_sqli import metinfo_login_check_sqli_BaseVerify

#用友 vulns
from .yonyou.yonyou_icc_struts2 import yonyou_icc_struts2_BaseVerify
from .yonyou.yonyou_user_ids_sqli import yonyou_user_ids_sqli_BaseVerify
from .yonyou.yonyou_multi_union_sqli import yonyou_multi_union_sqli_BaseVerify
from .yonyou.yonyou_initData_disclosure import yonyou_initData_disclosure_BaseVerify
from .yonyou.yonyou_createMysql_disclosure import yonyou_createMysql_disclosure_BaseVerify
from .yonyou.yonyou_test_sqli import yonyou_test_sqli_BaseVerify
from .yonyou.yonyou_getemaildata_fileread import yonyou_getemaildata_fileread_BaseVerify
from .yonyou.yonyou_ehr_ELTextFile import yonyou_ehr_ELTextFile_BaseVerify
from .yonyou.yonyou_a8_CmxUser_sqli import yonyou_a8_CmxUser_sqli_BaseVerify
from .yonyou.yonyou_cm_info_content_sqli import yonyou_cm_info_content_sqli_BaseVerify
from .yonyou.yonyou_a8_personService_xxe import yonyou_a8_personService_xxe_BaseVerify
from .yonyou.yonyou_u8_CmxItem_sqli import yonyou_u8_CmxItem_sqli_BaseVerify
from .yonyou.yonyou_fe_treeXml_sqli import yonyou_fe_treeXml_sqli_BaseVerify
from .yonyou.yonyou_ehr_resetpwd_sqli import yonyou_ehr_resetpwd_sqli_BaseVerify
from .yonyou.yonyou_nc_NCFindWeb_fileread import yonyou_nc_NCFindWeb_fileread_BaseVerify
from .yonyou.yonyou_a8_logs_disclosure import yonyou_a8_logs_disclosure_BaseVerify
from .yonyou.yonyou_status_default_pwd import yonyou_status_default_pwd_BaseVerify

#v2tech vulns
from .v2tech.v2Conference_sqli_xxe import v2Conference_sqli_xxe_BaseVerify

#digital campus vulns
from .digital_campus.digital_campus_log_disclosure import digital_campus_log_disclosure_BaseVerify
from .digital_campus.digital_campus_systemcodelist_sqli import digital_campus_systemcodelist_sqli_BaseVerify

#jeecms vulns
from .jeecms.jeecms_fpath_filedownload import jeecms_fpath_filedownload_BaseVerify

#jeecg vulns
from .jeecg.jeecg_pwd_reset import jeecg_pwd_reset_BaseVerify

#shopex vulns
from .shopex.shopex_phpinfo_disclosure import shopex_phpinfo_disclosure_BaseVerify

#FineCMS vulns
from .finecms.finecms_uploadfile import finecms_uploadfile_BaseVerify

#hanweb vulns
from .hanweb.hanweb_readxml_fileread import hanweb_readxml_fileread_BaseVerify
from .hanweb.hanweb_downfile_filedownload import hanweb_downfile_filedownload_BaseVerify
from .hanweb.hanweb_VerifyCodeServlet_install import hanweb_VerifyCodeServlet_install_BaseVerify

#php168 vulns
from .php168.php168_login_getshell import php168_login_getshell_BaseVerify

#dedecms vulns
from .dedecms.dedecms_version import dedecms_version_BaseVerify
from .dedecms.dedecms_recommend_sqli import dedecms_recommend_sqli_BaseVerify
from .dedecms.dedecms_download_redirect import dedecms_download_redirect_BaseVerify
from .dedecms.dedecms_error_trace_disclosure import dedecms_error_trace_disclosure_BaseVerify
from .dedecms.dedecms_search_typeArr_sqli import dedecms_search_typeArr_sqli_BaseVerify

#umail vulns
from .umail.umail_physical_path import umail_physical_path_BaseVerify
from .umail.umail_sessionid_access import umail_sessionid_access_BaseVerify

#fsmcms vulns
from .fsmcms.fsmcms_p_replydetail_sqli import fsmcms_p_replydetail_sqli_BaseVerify
from .fsmcms.fsmcms_setup_reinstall import fsmcms_setup_reinstall_BaseVerify
from .fsmcms.fsmcms_columninfo_sqli import fsmcms_columninfo_sqli_BaseVerify

#qibocms vulns
from .qibocms.qibocms_search_sqli import qibocms_search_sqli_BaseVerify
from .qibocms.qibocms_js_f_id_sqli import qibocms_js_f_id_sqli_BaseVerify
from .qibocms.qibocms_s_fids_sqli import qibocms_s_fids_sqli_BaseVerify
from .qibocms.qibocms_search_code_exec import qibocms_search_code_exec_BaseVerify

#inspur vulns
from .inspur.inspur_multi_sqli import inspur_multi_sqli_BaseVerify
from .inspur.inspur_ecgap_displayNewsPic_sqli import inspur_ecgap_displayNewsPic_sqli_BaseVerify

#gobetters vulns
from .gobetters.gobetters_multi_sqli import gobetters_multi_sqli_BaseVerify

#lbcms vulns
from .lbcms.lbcms_webwsfw_bssh_sqli import lbcms_webwsfw_bssh_sqli_BaseVerify

#dswjcms vulns
from .dswjcms.dswjcms_p2p_multi_sqli import dswjcms_p2p_multi_sqli_BaseVerify

#wordpress vulns
from .wordpress.wordpress_plugin_azonpop_sqli import wordpress_plugin_azonpop_sqli_BaseVerify
from .wordpress.wordpress_plugin_ShortCode_lfi import wordpress_plugin_ShortCode_lfi_BaseVerify
from .wordpress.wordpress_url_redirect import wordpress_url_redirect_BaseVerify
from .wordpress.wordpress_woocommerce_code_exec import wordpress_woocommerce_code_exec_BaseVerify
from .wordpress.wordpress_plugin_mailpress_rce import wordpress_plugin_mailpress_rce_BaseVerify
from .wordpress.wordpress_admin_ajax_filedownload import wordpress_admin_ajax_filedownload_BaseVerify
from .wordpress.wordpress_restapi_sqli import wordpress_restapi_sqli_BaseVerify
from .wordpress.wordpress_display_widgets_backdoor import wordpress_display_widgets_backdoor_BaseVerify

#票友 vulns
from .piaoyou.piaoyou_multi_sqli import piaoyou_multi_sqli_BaseVerify
from .piaoyou.piaoyou_ten_sqli import piaoyou_ten_sqli_BaseVerify
from .piaoyou.piaoyou_six_sqli import piaoyou_six_sqli_BaseVerify
from .piaoyou.piaoyou_six2_sqli import piaoyou_six2_sqli_BaseVerify
from .piaoyou.piaoyou_int_order_sqli import piaoyou_int_order_sqli_BaseVerify
from .piaoyou.piaoyou_newsview_list import piaoyou_newsview_list_BaseVerify

#TCExam vulns
from .tcexam.tcexam_reinstall_getshell import tcexam_reinstall_getshell_BaseVerify

#最土团购 vulns
from .zuitu.zuitu_coupon_id_sqli import zuitu_coupon_id_sqli_BaseVerify

#iwms vulns
from .iwms.iwms_bypass_js_delete import iwms_bypass_js_delete_BaseVerify

#cxplus vulns
from .xplus.xplus_2003_getshell import xplus_2003_getshell_BaseVerify
from .xplus.xplus_mysql_mssql_sqli import xplus_mysql_mssql_sqli_BaseVerify

#东软uniportal vulns
from .uniportal.uniportal_bypass_priv_sqli import uniportal_bypass_priv_sqli_BaseVerify

#pageadmin vulns
from .pageadmin.pageadmin_forge_viewstate import pageadmin_forge_viewstate_BaseVerify

#ruvar vulns
from .ruvar.ruvar_oa_multi_sqli import ruvar_oa_multi_sqli_BaseVerify
from .ruvar.ruvar_oa_multi_sqli2 import ruvar_oa_multi_sqli2_BaseVerify
from .ruvar.ruvar_oa_multi_sqli3 import ruvar_oa_multi_sqli3_BaseVerify

#jumboecms vulns
from .jumboecms.jumboecms_slide_id_sqli import jumboecms_slide_id_sqli_BaseVerify

#joomla vulns
from .joomla.joomla_com_docman_lfi import joomla_com_docman_lfi_BaseVerify
from .joomla.joomla_index_list_sqli import joomla_index_list_sqli_BaseVerify

#360shop vulns
from .shop360.shop360_do_filedownload import shop360_do_filedownload_BaseVerify

#pstar vulns
from .pstar.pstar_warehouse_msg_01_sqli import pstar_warehouse_msg_01_sqli_BaseVerify
from .pstar.pstar_isfLclInfo_sqli import pstar_isfLclInfo_sqli_BaseVerify
from .pstar.pstar_qcustoms_sqli import pstar_qcustoms_sqli_BaseVerify

#trs vulns
from .trs.trs_wcm_pre_as_lfi import trs_wcm_pre_as_lfi_BaseVerify
from .trs.trs_inforadar_disclosure import trs_inforadar_disclosure_BaseVerify
from .trs.trs_lunwen_papercon_sqli import trs_lunwen_papercon_sqli_BaseVerify
from .trs.trs_infogate_xxe import trs_infogate_xxe_BaseVerify
from .trs.trs_infogate_register import trs_infogate_register_BaseVerify
from .trs.trs_was5_config_disclosure import trs_was5_config_disclosure_BaseVerify
from .trs.trs_wcm_default_user import trs_wcm_default_user_BaseVerify
from .trs.trs_wcm_infoview_disclosure import trs_wcm_infoview_disclosure_BaseVerify
from .trs.trs_was40_passwd_disclosure import trs_was40_passwd_disclosure_BaseVerify
from .trs.trs_was40_tree_disclosure import trs_was40_tree_disclosure_BaseVerify
from .trs.trs_ids_auth_disclosure import trs_ids_auth_disclosure_BaseVerify
from .trs.trs_was5_download_templet import trs_was5_download_templet_BaseVerify
from .trs.trs_wcm_service_writefile import trs_wcm_service_writefile_BaseVerify

#易创思 vulns
from .ecscms.ecscms_MoreIndex_sqli import ecscms_MoreIndex_sqli_BaseVerify

#金窗教务系统 vulns
from .gowinsoft_jw.gowinsoft_jw_multi_sqli import gowinsoft_jw_multi_sqli_BaseVerify

#siteserver vulns
from .siteserver.siteserver_background_taskLog_sqli import siteserver_background_taskLog_sqli_BaseVerify
from .siteserver.siteserver_background_log_sqli import siteserver_background_log_sqli_BaseVerify
from .siteserver.siteserver_UserNameCollection_sqli import siteserver_UserNameCollection_sqli_BaseVerify
from .siteserver.siteserver_background_keywordsFilting_sqli import siteserver_background_keywordsFilting_sqli_BaseVerify
from .siteserver.siteserver_background_administrator_sqli import siteserver_background_administrator_sqli_BaseVerify

#nitc vulns
from .nitc.nitc_suggestwordList_sqli import nitc_suggestwordList_sqli_BaseVerify
from .nitc.nitc_index_language_id_sqli import nitc_index_language_id_sqli_BaseVerify

#南大之星 vulns
from .ndstar.ndstar_six_sqli import ndstar_six_sqli_BaseVerify

#安财软件 vulns
from .acsoft.acsoft_GetXMLList_fileread import acsoft_GetXMLList_fileread_BaseVerify
from .acsoft.acsoft_GetFile_fileread import acsoft_GetFile_fileread_BaseVerify
from .acsoft.acsoft_GetFileContent_fileread import acsoft_GetFileContent_fileread_BaseVerify

#英福金银花ETMV9数字化校园平台
from .etmdcp.etmdcp_Load_filedownload import etmdcp_Load_filedownload_BaseVerify

#speedcms vulns
from .speedcms.speedcms_list_cid_sqli import speedcms_list_cid_sqli_BaseVerify

#任我行 vulns
from .weway.weway_PictureView1_filedownload import weway_PictureView1_filedownload_BaseVerify

#esccms vulns
from .esccms.esccms_selectunitmember_unauth import esccms_selectunitmember_unauth_BaseVerify

#wecenter vulns
from .wecenter.wecenter_topic_id_sqli import wecenter_topic_id_sqli_BaseVerify

#shopnum1 vulns
from .shopnum.shopnum_ShoppingCart1_sqli import shopnum_ShoppingCart1_sqli_BaseVerify
from .shopnum.shopnum_ProductListCategory_sqli import shopnum_ProductListCategory_sqli_BaseVerify
from .shopnum.shopnum_GuidBuyList_sqli import shopnum_GuidBuyList_sqli_BaseVerify
from .shopnum.shopnum_ProductDetail_sqli import shopnum_ProductDetail_sqli_BaseVerify

#fastmeeting vulns
from .fastmeeting.fastmeeting_download_filedownload import fastmeeting_download_filedownload_BaseVerify


#远古 vulns
from .viewgood.viewgood_two_sqli import viewgood_two_sqli_BaseVerify
from .viewgood.viewgood_pic_proxy_sqli import viewgood_pic_proxy_sqli_BaseVerify
from .viewgood.viewgood_GetCaption_sqli import viewgood_GetCaption_sqli_BaseVerify

#shop7z vulns
from .shop7z.shop7z_order_checknoprint_sqli import shop7z_order_checknoprint_sqli_BaseVerify

#dreamgallery vulns
from .dreamgallery.dreamgallery_album_id_sqli import dreamgallery_album_id_sqli_BaseVerify

#kxmail vulns
from .kxmail.kxmail_login_server_sqli import kxmail_login_server_sqli_BaseVerify

#shopnc vulns
from .shopnc.shopnc_index_class_id_sqli import shopnc_index_class_id_sqli_BaseVerify

#shadowsit vulns
from .shadowsit.shadowsit_selector_lfi import shadowsit_selector_lfi_BaseVerify

#phpcms vulns
from .phpcms.phpcms_digg_add_sqli import phpcms_digg_add_sqli_BaseVerify
from .phpcms.phpcms_authkey_disclosure import phpcms_authkey_disclosure_BaseVerify
from .phpcms.phpcms_flash_upload_sqli import phpcms_flash_upload_sqli_BaseVerify
from .phpcms.phpcms_product_code_exec import phpcms_product_code_exec_BaseVerify
from .phpcms.phpcms_v96_sqli import phpcms_v96_sqli_BaseVerify
from .phpcms.phpcms_v961_fileread import phpcms_v961_fileread_BaseVerify
from .phpcms.phpcms_v9_flash_xss import phpcms_v9_flash_xss_BaseVerify

#seacms vulns
from .seacms.seacms_search_code_exec import seacms_search_code_exec_BaseVerify
from .seacms.seacms_order_code_exec import seacms_order_code_exec_BaseVerify
from .seacms.seacms_search_jq_code_exec import seacms_search_jq_code_exec_BaseVerify

#cmseasy vulns
from .cmseasy.cmseasy_header_detail_sqli import cmseasy_header_detail_sqli_BaseVerify

#phpmyadmin vulns
from .phpmyadmin.phpmyadmin_setup_lfi import phpmyadmin_setup_lfi_BaseVerify

#opensns vulns
from .opensns.opensns_index_arearank import opensns_index_arearank_BaseVerify
from .opensns.opensns_index_getshell import opensns_index_getshell_BaseVerify

#thinksns vulns
from .thinksns.thinksns_category_code_exec import thinksns_category_code_exec_BaseVerify

#others vulns
from .others.domino_unauth import domino_unauth_BaseVerify
from .others.hjsoft_sqli import hjsoft_sqli_BaseVerify
from .others.hnkj_researchinfo_dan_sqli import hnkj_researchinfo_dan_sqli_BaseVerify
from .others.gpcsoft_ewebeditor_weak import gpcsoft_ewebeditor_weak_BaseVerify
from .others.rap_interface_struts_exec import rap_interface_struts_exec_BaseVerify
from .others.hongan_dlp_struts_exec import hongan_dlp_struts_exec_BaseVerify
from .others.jiuyu_library_struts_exec import jiuyu_library_struts_exec_BaseVerify
from .others.yaojie_steel_struts_exec import yaojie_steel_struts_exec_BaseVerify
from .others.dkcms_database_disclosure import dkcms_database_disclosure_BaseVerify
from .others.damall_selloffer_sqli import damall_selloffer_sqli_BaseVerify
from .others.yeu_disclosure_uid import yeu_disclosure_uid_BaseVerify
from .others.clib_kinweblistaction_download import clib_kinweblistaction_download_BaseVerify
from .others.euse_study_multi_sqli import euse_study_multi_sqli_BaseVerify
from .others.suntown_upfile_fileupload import suntown_upfile_fileupload_BaseVerify
from .others.skytech_bypass_priv import skytech_bypass_priv_BaseVerify
from .others.mallbuilder_change_status_sqli import mallbuilder_change_status_sqli_BaseVerify
from .others.efuture_downloadAct_filedownload import efuture_downloadAct_filedownload_BaseVerify
from .others.kj65n_monitor_sqli import kj65n_monitor_sqli_BaseVerify
from .others.sinda_downloadfile_download import sinda_downloadfile_download_BaseVerify
from .others.lianbang_multi_bypass_priv import lianbang_multi_bypass_priv_BaseVerify
from .others.star_PostSuggestion_sqli import star_PostSuggestion_sqli_BaseVerify
from .others.hezhong_list_id_sqli import hezhong_list_id_sqli_BaseVerify
from .others.cicro_DownLoad_filedownload import cicro_DownLoad_filedownload_BaseVerify
from .others.huaficms_bypass_js import huaficms_bypass_js_BaseVerify
from .others.nongyou_multi_sqli import nongyou_multi_sqli_BaseVerify
from .others.zfcgxt_UserSecurityController_getpass import zfcgxt_UserSecurityController_getpass_BaseVerify
from .others.mainone_b2b_Default_sqli import mainone_b2b_Default_sqli_BaseVerify
from .others.mainone_SupplyList_sqli import mainone_SupplyList_sqli_BaseVerify
from .others.workyi_multi_sqli import workyi_multi_sqli_BaseVerify
from .others.newedos_multi_sqli import newedos_multi_sqli_BaseVerify
from .others.xtcms_download_filedownload import xtcms_download_filedownload_BaseVerify
from .others.gn_consulting_sqli import gn_consulting_sqli_BaseVerify
from .others.caitong_multi_sqli import caitong_multi_sqli_BaseVerify
from .others.anmai_teachingtechnology_sqli import anmai_teachingtechnology_sqli_BaseVerify
from .others.alkawebs_viewnews_sqli import alkawebs_viewnews_sqli_BaseVerify
from .others.caitong_multi_sleep_sqli import caitong_multi_sleep_sqli_BaseVerify
from .others.clib_kindaction_fileread import clib_kindaction_fileread_BaseVerify
from .others.mainone_ProductList_sqli import mainone_ProductList_sqli_BaseVerify
from .others.eis_menu_left_edit_sqli import eis_menu_left_edit_sqli_BaseVerify
from .others.tianbo_Type_List_sqli import tianbo_Type_List_sqli_BaseVerify
from .others.tianbo_TCH_list_sqli import tianbo_TCH_list_sqli_BaseVerify
from .others.tianbo_Class_Info_sqli import tianbo_Class_Info_sqli_BaseVerify
from .others.tianbo_St_Info_sqli import tianbo_St_Info_sqli_BaseVerify
from .others.nongyou_Item2_sqli import nongyou_Item2_sqli_BaseVerify
from .others.gxwssb_fileDownloadmodel_download import gxwssb_fileDownloadmodel_download_BaseVerify
from .others.anmai_grghjl_stuNo_sqli import anmai_grghjl_stuNo_sqli_BaseVerify
from .others.nongyou_ShowLand_sqli import nongyou_ShowLand_sqli_BaseVerify
from .others.nongyou_sleep_sqli import nongyou_sleep_sqli_BaseVerify
from .others.zf_cms_FileDownload import zf_cms_FileDownload_BaseVerify
from .others.shiyou_list_keyWords_sqli import shiyou_list_keyWords_sqli_BaseVerify
from .others.zhuofan_downLoadFile_download import zhuofan_downLoadFile_download_BaseVerify
from .others.gevercms_downLoadFile_filedownload import gevercms_downLoadFile_filedownload_BaseVerify
from .others.ips_community_suite_code_exec import ips_community_suite_code_exec_BaseVerify
from .others.skytech_geren_list_page_sqli import skytech_geren_list_page_sqli_BaseVerify
from .others.xuezi_ceping_unauth import xuezi_ceping_unauth_BaseVerify
from .others.haohan_FileDown_filedownload import haohan_FileDown_filedownload_BaseVerify
from .others.mingteng_cookie_deception import mingteng_cookie_deception_BaseVerify
from .others.jxt1039_unauth import jxt1039_unauth_BaseVerify
from .others.tpshop_eval_stdin_code_exec import tpshop_eval_stdin_code_exec_BaseVerify
