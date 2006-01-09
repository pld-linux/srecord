Summary:	Manipulate EPROM load files
Summary(pl):	Operacje na plikach do programowania pamiêci (E)EPROM i Flash
Name:		srecord
Version:	1.23
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://srecord.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	fcca798d3cc3f186410b8ed0e1c2e793
Patch0:		%{name}-man_fastload.patch
URL:		http://srecord.sourceforge.net/
BuildRequires:  bison
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SRecord package is a collection of powerful tools for manipulating
EPROM load files.

- The SRecord package understands a number of file formats: Motorola
  S-Record, Intel, Tektronix, Binary. These file formats may be read and
  written. Also C array definitions, for output only.

- The SRecord package has a number of tools: srec_cat for copying and
  and converting files, srec_cmp for comparing files and srec_info for
  printing summaries.

- The SRecord package has a number for filters: checksum to add
  checksums to the data, crop to keep address ranges, exclude to remove
  address ranges, fill to plug holes in the data, length to insert the
  data length, maximum to insert the data address maximum, minimum to
  insert the data address minimum, offset to adjust addresses, and split
  for wide data buses and memory striping.

More than one filter may be applied to each input file. Different
filters may be applied to each input file. All filters may be applied
to all file formats.

%description -l pl
Pakiet SRecord to zbiór narzêdzi do modyfikacji plików u¿ywanych do
programowania pamiêci (E)EPROM i Flash.

- Odczytywane i zapisywane s± pliki w nastêpuj±cych formatach:
  Motorola S-Record, Intel, Tektronix, Binary.

- W pakiecie znajduj± siê nastêpuj±ce narzêdzia: srec_cat - do
  kopiowania i konwersji plików, srec_cmp - do porównywania plików,
  srec_info - do wy¶wietlania informacji o plikach.

- Dostêpne s± nastêpuj±ce filtry: cheksum - dodawanie sumy kontrolnej
  do danych, crop - usuwanie danych spoza podanego zakresu adresów,
  exclude - usuwanie danych z podanego zakresu adresów, fill -
  wype³nianie podanego zakresu adresów, length - dodawanie d³ugo¶ci
  danych, maximum - dodawanie najwiêkszego adresu z danych wej¶ciowych,
  minimum - dodawanie najmniejszego adresu z danych wej¶ciowych, offset
  - modyfikowanie adresów o podan± warto¶æ, split - rozdzielanie danych
  wej¶ciowych na podzbiory.

Dla ka¿dego pliku wej¶ciowego mo¿e byæ dodanych po kilka filtrów
wej¶ciowych. Ka¿dy z filtrów mo¿e byæ stosowany do ka¿dego z formatów
plików.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUILDING README
%attr(755,root,root) %{_bindir}/srec_cat
%attr(755,root,root) %{_bindir}/srec_cmp
%attr(755,root,root) %{_bindir}/srec_info
%{_mandir}/man1/*
%{_mandir}/man5/*
