%define upstream_name    Perl-OSType
%define upstream_version 1.002

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Map Perl operating system names to generic types
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Exporter)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::More)
BuildRequires: perl(constant)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*


