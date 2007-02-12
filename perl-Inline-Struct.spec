#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Struct
Summary:	Inline::Struct Perl module
Summary(cs.UTF-8):   Modul Inline::Struct pro Perl
Summary(da.UTF-8):   Perlmodul Inline::Struct
Summary(de.UTF-8):   Inline::Struct Perl Modul
Summary(es.UTF-8):   Módulo de Perl Inline::Struct
Summary(fr.UTF-8):   Module Perl Inline::Struct
Summary(it.UTF-8):   Modulo di Perl Inline::Struct
Summary(ja.UTF-8):   Inline::Struct Perl モジュール
Summary(ko.UTF-8):   Inline::Struct 펄 모줄
Summary(nb.UTF-8):   Perlmodul Inline::Struct
Summary(pl.UTF-8):   Moduł Perla Inline::Struct
Summary(pt.UTF-8):   Módulo de Perl Inline::Struct
Summary(pt_BR.UTF-8):   Módulo Perl Inline::Struct
Summary(ru.UTF-8):   Модуль для Perl Inline::Struct
Summary(sv.UTF-8):   Inline::Struct Perlmodul
Summary(uk.UTF-8):   Модуль для Perl Inline::Struct
Summary(zh_CN.UTF-8):   Inline::Struct Perl 模块
Name:		perl-Inline-Struct
Version:	0.06
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a12b18f058361f4a3df4d39a67440bbd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Inline-C >= 0.42
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Inline-C >= 0.42
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Struct - Manipulate C structs directly from Perl.

%description -l pl.UTF-8
Moduł Inline::Struct - pozwalający na dostęp do struktur C z poziomu
Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{perl_vendorlib}/Inline/Struct.pm
%{perl_vendorlib}/Inline/Struct
%{_mandir}/man3/*
