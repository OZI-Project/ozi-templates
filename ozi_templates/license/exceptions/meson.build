# OZI 0.10
# Part of OZI-Templates.
# See LICENSE.txt in the project root for details.
# DO NOT EDIT BY HAND - This file was generated for use with OZI tools.
# ozi-fix -> meson rewrite is the standard editing pipeline.
source_files = [
    '389-exception.txt',
    'Asterisk-exception.txt',
    'Asterisk-linking-protocols-exception.txt',
    'Autoconf-exception-2.0.txt',
    'Autoconf-exception-3.0.txt',
    'Autoconf-exception-generic-3.0.txt',
    'Autoconf-exception-generic.txt',
    'Autoconf-exception-macro.txt',
    'Bison-exception-1.24.txt',
    'Bison-exception-2.2.txt',
    'Bootloader-exception.txt',
    'CLISP-exception-2.0.txt',
    'Classpath-exception-2.0.txt',
    'DigiRule-FOSS-exception.txt',
    'FLTK-exception.txt',
    'Fawkes-Runtime-exception.txt',
    'Font-exception-2.0.txt',
    'GCC-exception-2.0-note.txt',
    'GCC-exception-2.0.txt',
    'GCC-exception-3.1.txt',
    'GNAT-exception.txt',
    'GNOME-examples-exception.txt',
    'GNU-compiler-exception.txt',
    'GPL-3.0-interface-exception.txt',
    'GPL-3.0-linking-exception.txt',
    'GPL-3.0-linking-source-exception.txt',
    'GPL-CC-1.0.txt',
    'GStreamer-exception-2005.txt',
    'GStreamer-exception-2008.txt',
    'Gmsh-exception.txt',
    'KiCad-libraries-exception.txt',
    'LGPL-3.0-linking-exception.txt',
    'LLGPL.txt',
    'LLVM-exception.txt',
    'LZMA-exception.txt',
    'Libtool-exception.txt',
    'Linux-syscall-note.txt',
    'MPL-2.0-no-copyleft-exception.txt',
    'Nokia-Qt-exception-1.1.txt',
    'OCCT-exception-1.0.txt',
    'OCaml-LGPL-linking-exception.txt',
    'OpenJDK-assembly-exception-1.0.txt',
    'PCRE2-exception.txt',
    'PS-or-PDF-font-exception-20170817.txt',
    'QPL-1.0-INRIA-2004-exception.txt',
    'Qt-GPL-exception-1.0.txt',
    'Qt-LGPL-exception-1.1.txt',
    'Qwt-exception-1.0.txt',
    'RRDtool-FLOSS-exception-2.0.txt',
    'SANE-exception.txt',
    'SHL-2.0.txt',
    'SHL-2.1.txt',
    'SWI-exception.txt',
    'Swift-exception.txt',
    'Texinfo-exception.txt',
    'UBDL-exception.txt',
    'Universal-FOSS-exception-1.0.txt',
    'WxWindows-exception-3.1.txt',
    'cryptsetup-OpenSSL-exception.txt',
    'eCos-exception-2.0.txt',
    'erlang-otp-linking-exception.txt',
    'fmt-exception.txt',
    'freertos-exception-2.0.txt',
    'gnu-javamail-exception.txt',
    'i2p-gpl-java-exception.txt',
    'libpri-OpenH323-exception.txt',
    'mif-exception.txt',
    'openvpn-openssl-exception.txt',
    'romic-exception.txt',
    'stunnel-exception.txt',
    'u-boot-exception-2.0.txt',
    'vsftpd-openssl-exception.txt',
    'x11vnc-openssl-exception.txt',
]
foreach file : source_files
    fs.copyfile(file)
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(
            file,
            subdir: 'ozi_templates' / 'license' / 'exceptions',
        )
    endif
endforeach
