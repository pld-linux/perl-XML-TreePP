#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	XML
%define		pnam	TreePP
Summary:	XML::TreePP -- Pure Perl implementation for parsing/writing XML documents
Name:		perl-XML-TreePP
Version:	0.41
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3e999ac519163cf3cab70d3ee8d40b34
URL:		http://search.cpan.org/dist/XML-TreePP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-libwww >= 5.802
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::TreePP module parses an XML document and expands it for a hash tree.
This generates an XML document from a hash tree as the opposite way around.
This is a pure Perl implementation and requires no modules depended.
This can also fetch and parse an XML document from remote web server
like the XMLHttpRequest object does at JavaScript language.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
