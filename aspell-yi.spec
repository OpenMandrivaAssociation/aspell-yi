%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.01.1-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Yiddish
%define languagecode yi
%define lc_ctype yi_US

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.01.1.1
Release:       %mkrel 2
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright 
%{_libdir}/aspell-%{aspell_ver}/*


