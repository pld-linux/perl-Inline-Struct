#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pname	Struct
Summary:	Inline::Struct Perl module
Summary(cs):	Modul Inline::Struct pro Perl
Summary(da):	Perlmodul Inline::Struct
Summary(de):	Inline::Struct Perl Modul
Summary(es):	Módulo de Perl Inline::Struct
Summary(fr):	Module Perl Inline::Struct
Summary(it):	Modulo di Perl Inline::Struct
Summary(ja):	Inline::Struct Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::Struct ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Inline::Struct
Summary(pl):	Modu³ Perla Inline::Struct
Summary(pt):	Módulo de Perl Inline::Struct
Summary(pt_BR):	Módulo Perl Inline::Struct
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::Struct
Summary(sv):	Inline::Struct Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::Struct
Summary(zh_CN):	Inline::Struct Perl Ä£¿é
Name:		perl-Inline-Struct
Version:	0.06
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline-C >= 0.42
BuildRequires:	rpm-perlprov >= 4.0.2-104
Requires:	perl-Inline-C >= 0.42
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Struct - Manipulate C structs directly from Perl.

%description -l pl
Modu³ Inline::Struct - pozwalaj±cy na dostêp do struktur C z poziomu
Perla.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
%{__perl} Makefile.PL </dev/null
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{perl_sitelib}/Inline/Struct.pm
%{perl_sitelib}/Inline/Struct
%{_mandir}/man3/*
