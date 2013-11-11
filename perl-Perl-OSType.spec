%define upstream_name    Perl-OSType
%define upstream_version 1.006

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Map Perl operating system names to generic types
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/Perl-OSType-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Capture::Tiny)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(constant)
BuildArch:	noarch

%description
Modules that provide OS-specific behaviors often need to know if the
current operating system matches a more generic type of operating systems.
For example, 'linux' is a type of 'Unix' operating system and so is
'freebsd'.

This module provides a mapping between an operating system name as given by
'$^O' and a more generic type. The initial version is based on the OS type
mappings provided in the Module::Build manpage and the ExtUtils::CBuilder
manpage. (Thus, Microsoft operating systems are given the type 'Windows'
rather than 'Win32'.)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Fri Jun 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-1mdv2012.0
+ Revision: 685815
- import perl-Perl-OSType




