#
# DO NOT MODIFY! THIS IS AUTOGENERATED FILE!
#

from .libcefdef import *
from .libcefstruct import *
from .libcefversion import *
from . import libcefsizes

from .Handlers import *

@ CEFENTRY(c_int, "cef_version_info", c_int)
def version_info(entry:int):
    return version_info._api_(entry)

@ CEFENTRY(POINTER(c_byte), "cef_api_hash", c_int)
def api_hash(entry:int):
    return api_hash._api_(entry)


# CefExecuteProcess
@ CEFENTRY(c_int, "cef_execute_process", POINTER(cef_main_args_t), POINTER(cef_app_t), c_void_p)
def execute_process(args, application, windows_sandbox_info):
    return execute_process._api_(args, application, windows_sandbox_info)

# CefInitialize
@ CEFENTRY(c_int, "cef_initialize", POINTER(cef_main_args_t), POINTER(cef_settings_t), POINTER(cef_app_t), c_void_p)
def initialize(args, settings, application, windows_sandbox_info):
    return initialize._api_(args, settings, application, windows_sandbox_info)

# CefShutdown
@ CEFENTRY(c_void, "cef_shutdown", )
def shutdown():
    shutdown._api_()

# CefDoMessageLoopWork
@ CEFENTRY(c_void, "cef_do_message_loop_work", )
def do_message_loop_work():
    do_message_loop_work._api_()

# CefRunMessageLoop
@ CEFENTRY(c_void, "cef_run_message_loop", )
def run_message_loop():
    run_message_loop._api_()

# CefQuitMessageLoop
@ CEFENTRY(c_void, "cef_quit_message_loop", )
def quit_message_loop():
    quit_message_loop._api_()

# CefSetOSModalLoop
@ CEFENTRY(c_void, "cef_set_osmodal_loop", c_int)
def set_osmodal_loop(osModalLoop):
    set_osmodal_loop._api_(osModalLoop)

# CefEnableHighDPISupport
@ CEFENTRY(c_void, "cef_enable_highdpi_support", )
def enable_highdpi_support():
    enable_highdpi_support._api_()

# CefCrashReportingEnabled
@ CEFENTRY(c_int, "cef_crash_reporting_enabled", )
def crash_reporting_enabled():
    return crash_reporting_enabled._api_()

# CefSetCrashKeyValue
@ CEFENTRY(c_void, "cef_set_crash_key_value", POINTER(cef_string_t), POINTER(cef_string_t))
def set_crash_key_value(key, value):
    set_crash_key_value._api_(key, value)

# CefCreateDirectory
@ CEFENTRY(c_int, "cef_create_directory", POINTER(cef_string_t))
def create_directory(full_path):
    return create_directory._api_(full_path)

# CefGetTempDirectory
@ CEFENTRY(c_int, "cef_get_temp_directory", POINTER(cef_string_t))
def get_temp_directory(temp_dir):
    return get_temp_directory._api_(temp_dir)

# CefCreateNewTempDirectory
@ CEFENTRY(c_int, "cef_create_new_temp_directory", POINTER(cef_string_t), POINTER(cef_string_t))
def create_new_temp_directory(prefix, new_temp_path):
    return create_new_temp_directory._api_(prefix, new_temp_path)

# CefCreateTempDirectoryInDirectory
@ CEFENTRY(c_int, "cef_create_temp_directory_in_directory", POINTER(cef_string_t), POINTER(cef_string_t), POINTER(cef_string_t))
def create_temp_directory_in_directory(base_dir, prefix, new_dir):
    return create_temp_directory_in_directory._api_(base_dir, prefix, new_dir)

# CefDirectoryExists
@ CEFENTRY(c_int, "cef_directory_exists", POINTER(cef_string_t))
def directory_exists(path):
    return directory_exists._api_(path)

# CefDeleteFile
@ CEFENTRY(c_int, "cef_delete_file", POINTER(cef_string_t), c_int)
def delete_file(path, recursive):
    return delete_file._api_(path, recursive)

# CefZipDirectory
@ CEFENTRY(c_int, "cef_zip_directory", POINTER(cef_string_t), POINTER(cef_string_t), c_int)
def zip_directory(src_dir, dest_file, include_hidden_files):
    return zip_directory._api_(src_dir, dest_file, include_hidden_files)

# CefLoadCRLSetsFile
@ CEFENTRY(c_void, "cef_load_crlsets_file", POINTER(cef_string_t))
def load_crlsets_file(path):
    load_crlsets_file._api_(path)

# CefIsRTL
@ CEFENTRY(c_int, "cef_is_rtl", )
def is_rtl():
    return is_rtl._api_()

# CefAddCrossOriginWhitelistEntry
@ CEFENTRY(c_int, "cef_add_cross_origin_whitelist_entry", POINTER(cef_string_t), POINTER(cef_string_t), POINTER(cef_string_t), c_int)
def add_cross_origin_whitelist_entry(source_origin, target_protocol, target_domain, allow_target_subdomains):
    return add_cross_origin_whitelist_entry._api_(source_origin, target_protocol, target_domain, allow_target_subdomains)

# CefRemoveCrossOriginWhitelistEntry
@ CEFENTRY(c_int, "cef_remove_cross_origin_whitelist_entry", POINTER(cef_string_t), POINTER(cef_string_t), POINTER(cef_string_t), c_int)
def remove_cross_origin_whitelist_entry(source_origin, target_protocol, target_domain, allow_target_subdomains):
    return remove_cross_origin_whitelist_entry._api_(source_origin, target_protocol, target_domain, allow_target_subdomains)

# CefClearCrossOriginWhitelist
@ CEFENTRY(c_int, "cef_clear_cross_origin_whitelist", )
def clear_cross_origin_whitelist():
    return clear_cross_origin_whitelist._api_()

# CefParseURL
@ CEFENTRY(c_int, "cef_parse_url", POINTER(cef_string_t), POINTER(cef_urlparts_t))
def parse_url(url, parts):
    return parse_url._api_(url, parts)

# CefCreateURL
@ CEFENTRY(c_int, "cef_create_url", POINTER(cef_urlparts_t), POINTER(cef_string_t))
def create_url(parts, url):
    return create_url._api_(parts, url)

# CefFormatUrlForSecurityDisplay
@ CEFENTRY(POINTER(cef_string_userfree_t), "cef_format_url_for_security_display", POINTER(cef_string_t))
def format_url_for_security_display(origin_url):
    return format_url_for_security_display._api_(origin_url)

# CefGetMimeType
@ CEFENTRY(POINTER(cef_string_userfree_t), "cef_get_mime_type", POINTER(cef_string_t))
def get_mime_type(extension):
    return get_mime_type._api_(extension)

# CefGetExtensionsForMimeType
@ CEFENTRY(c_void, "cef_get_extensions_for_mime_type", POINTER(cef_string_t), cef_string_list_t)
def get_extensions_for_mime_type(mime_type, extensions):
    get_extensions_for_mime_type._api_(mime_type, extensions)

# CefBase64Encode
@ CEFENTRY(POINTER(cef_string_userfree_t), "cef_base64encode", c_void_p, c_size_t)
def base64encode(data, data_size):
    return base64encode._api_(data, data_size)

# CefBase64Decode
@ CEFENTRY(POINTER(cef_binary_value_t), "cef_base64decode", POINTER(cef_string_t))
def base64decode(data):
    return base64decode._api_(data)

# CefURIEncode
@ CEFENTRY(POINTER(cef_string_userfree_t), "cef_uriencode", POINTER(cef_string_t), c_int)
def uriencode(text, use_plus):
    return uriencode._api_(text, use_plus)

# CefURIDecode
@ CEFENTRY(POINTER(cef_string_userfree_t), "cef_uridecode", POINTER(cef_string_t), c_int, CefUriUnescapeRules)
def uridecode(text, convert_to_utf8, unescape_rule):
    return uridecode._api_(text, convert_to_utf8, unescape_rule)

# CefParseJSON
@ CEFENTRY(POINTER(cef_value_t), "cef_parse_json", POINTER(cef_string_t), CefJsonParserOptions)
def parse_json(json_string, options):
    return parse_json._api_(json_string, options)

# CefParseJSON
@ CEFENTRY(POINTER(cef_value_t), "cef_parse_json_buffer", c_void_p, c_size_t, CefJsonParserOptions)
def parse_json_buffer(json, json_size, options):
    return parse_json_buffer._api_(json, json_size, options)

# CefParseJSONAndReturnError
@ CEFENTRY(POINTER(cef_value_t), "cef_parse_jsonand_return_error", POINTER(cef_string_t), CefJsonParserOptions, POINTER(cef_string_t))
def parse_jsonand_return_error(json_string, options, error_msg_out):
    return parse_jsonand_return_error._api_(json_string, options, error_msg_out)

# CefWriteJSON
@ CEFENTRY(POINTER(cef_string_userfree_t), "cef_write_json", POINTER(cef_value_t), CefJsonWriterOptions)
def write_json(node, options):
    return write_json._api_(node, options)

# CefGetPath
@ CEFENTRY(c_int, "cef_get_path", CefPathKey, POINTER(cef_string_t))
def get_path(key, path):
    return get_path._api_(key, path)

# CefLaunchProcess
@ CEFENTRY(c_int, "cef_launch_process", POINTER(cef_command_line_t))
def launch_process(command_line):
    return launch_process._api_(command_line)

# CefRegisterSchemeHandlerFactory
@ CEFENTRY(c_int, "cef_register_scheme_handler_factory", POINTER(cef_string_t), POINTER(cef_string_t), POINTER(cef_scheme_handler_factory_t))
def register_scheme_handler_factory(scheme_name, domain_name, factory):
    return register_scheme_handler_factory._api_(scheme_name, domain_name, factory)

# CefClearSchemeHandlerFactories
@ CEFENTRY(c_int, "cef_clear_scheme_handler_factories", )
def clear_scheme_handler_factories():
    return clear_scheme_handler_factories._api_()

# CefIsCertStatusError
@ CEFENTRY(c_int, "cef_is_cert_status_error", CefCertStatus)
def is_cert_status_error(status):
    return is_cert_status_error._api_(status)

# CefCurrentlyOn
@ CEFENTRY(c_int, "cef_currently_on", CefThreadId)
def currently_on(threadId):
    return currently_on._api_(threadId)

# CefPostTask
@ CEFENTRY(c_int, "cef_post_task", CefThreadId, POINTER(cef_task_t))
def post_task(threadId, task):
    return post_task._api_(threadId, task)

# CefPostDelayedTask
@ CEFENTRY(c_int, "cef_post_delayed_task", CefThreadId, POINTER(cef_task_t), c_long)
def post_delayed_task(threadId, task, delay_ms):
    return post_delayed_task._api_(threadId, task, delay_ms)

# CefBeginTracing
@ CEFENTRY(c_int, "cef_begin_tracing", POINTER(cef_string_t), POINTER(cef_completion_callback_t))
def begin_tracing(categories, callback):
    return begin_tracing._api_(categories, callback)

# CefEndTracing
@ CEFENTRY(c_int, "cef_end_tracing", POINTER(cef_string_t), POINTER(cef_end_tracing_callback_t))
def end_tracing(tracing_file, callback):
    return end_tracing._api_(tracing_file, callback)

# CefNowFromSystemTraceTime
@ CEFENTRY(c_long, "cef_now_from_system_trace_time", )
def now_from_system_trace_time():
    return now_from_system_trace_time._api_()

# CefRegisterExtension
@ CEFENTRY(c_int, "cef_register_extension", POINTER(cef_string_t), POINTER(cef_string_t), POINTER(cef_v8handler_t))
def register_extension(extension_name, javascript_code, handler):
    return register_extension._api_(extension_name, javascript_code, handler)
