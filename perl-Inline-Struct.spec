%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pname	Struct
Summary:	Inline::Struct perl module
Summary(pl):	Modu³ perla Inline::Struct
Name:		perl-Inline-Struct
Version:	0.06
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline-C >= 0.42
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL </dev/null
%{__make}

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
