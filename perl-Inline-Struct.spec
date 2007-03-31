#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Struct
Summary:	Inline::Struct - Manipulate C structs directly from Perl
Summary(pl.UTF-8):	Inline::Struct - dostęp do struktur C z poziomu Perla
Name:		perl-Inline-Struct
Version:	0.06
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Inline/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a12b18f058361f4a3df4d39a67440bbd
URL:		http://search.cpan.org/dist/Inline-Struct/
BuildRequires:	perl-Inline-C >= 0.42
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Inline-C >= 0.42
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Struct is not a new language. It's a language extension
designed to be used by Inline::C. It parses struct definitions and
creates typemaps and XS code which bind each struct into a Perl class.
This code is passed to Inline::C, which compiles it in the normal way.

%description -l pl.UTF-8
Inline::Struct nie jest nowym językiem, lecz rozszerzeniem języka
zaprojektowanym do używania przez Inline::C. Analizuje definicje
struktur i tworzy mapy typów oraz kod XS przypisujący każdą strukturę
do klasy perlowej. Kod ten jest przekazywany do Inline::C, który
kompiluje go w zwykły sposób.

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
