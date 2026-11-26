#!/usr/bin/env tclsh
set query ""
if {[info exists env(QUERY_STRING)]} { set query $env(QUERY_STRING) }

if {[regexp {\mcmd=download\M} $query]} {
  # forward to the download page
  puts -nonewline "Content-Type: text/html; charset=utf-8\r\n\r\n"
  puts "<html><head><meta http-equiv='refresh' content='0; url=https://github.com/4nn4n45/homematic_check_mk/releases' /></head></html>"
} else {
  # version of the latest release, without the leading v; N/A on any failure
  set infoUrl https://api.github.com/repos/4nn4n45/homematic_check_mk/releases/latest
  set infoError [catch {
    set info [exec curl -sL --max-time 10 $infoUrl]
    if {![regexp {"tag_name"\s*:\s*"v?([0-9][0-9.]*)"} $info -> version]} { error "no tag" }
  }]
  puts -nonewline "Content-Type: text/plain; charset=utf-8\r\n\r\n"
  if {$infoError} { puts "N/A" } else { puts $version }
}
