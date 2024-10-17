Name:		texlive-bibtex
Version:	70015
Release:	1
Summary:	Process bibliographies for LaTeX, etc
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/base
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-bibtex.bin

%description
BibTeX allows the user to store his citation data in generic
form, while printing citations in a document in the form
specified by a BibTeX style, to be specified in the document
itself (one often needs a LaTeX citation-style package, such as
natbib as well). BibTeX itself is an ASCII-only program; there
is, however, a version that copes with 8-bit character sets.
However, BibTeX's facilities rapidly run out as one moves away
from simple ASCII (for example, in the various national sorting
rules for languages expressed in different parts of ISO-8859 --
the "ISO Latin" series). For more flexibility, the user is
urged to consider using biber with biblatex to typeset its
output. In particular, it is best to avoid BibTeX in favour of
biblatex, if at all possible.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/base/xampl.bib
%{_texmfdistdir}/bibtex/bst/base/abbrv.bst
%{_texmfdistdir}/bibtex/bst/base/acm.bst
%{_texmfdistdir}/bibtex/bst/base/alpha.bst
%{_texmfdistdir}/bibtex/bst/base/apalike.bst
%{_texmfdistdir}/bibtex/bst/base/ieeetr.bst
%{_texmfdistdir}/bibtex/bst/base/plain.bst
%{_texmfdistdir}/bibtex/bst/base/siam.bst
%{_texmfdistdir}/bibtex/bst/base/unsrt.bst
%doc %{_texmfdistdir}/doc/bibtex/base/README
%doc %{_texmfdistdir}/doc/bibtex/base/btxbst.doc
%doc %{_texmfdistdir}/doc/bibtex/base/btxdoc.bib
%doc %{_texmfdistdir}/doc/bibtex/base/btxdoc.pdf
%doc %{_texmfdistdir}/doc/bibtex/base/btxdoc.tex
%doc %{_texmfdistdir}/doc/bibtex/base/btxhak.pdf
%doc %{_texmfdistdir}/doc/bibtex/base/btxhak.tex
%doc %{_mandir}/man1/bibtex.1*
%doc %{_texmfdistdir}/doc/man/man1/bibtex.man1.pdf
%doc %{_texmfdistdir}/tex/generic/bibtex/apalike.sty
%doc %{_texmfdistdir}/tex/generic/bibtex/apalike.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
