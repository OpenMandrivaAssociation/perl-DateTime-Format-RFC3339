%define upstream_name    DateTime-Format-RFC3339
%define upstream_version v1.0.4

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Parse and format RFC3339 datetime strings
License:	Public domain
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(version)
BuildArch:	noarch

%description
This module understands the RFC3339 date/time format, an ISO 8601 profile,
defined at http://tools.ietf.org/html/rfc3339 .

It can be used to parse these formats in order to create the appropriate
objects.

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
%doc README Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.0.4-2mdv2011.0
+ Revision: 654305
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 624987
- import perl-DateTime-Format-RFC3339

