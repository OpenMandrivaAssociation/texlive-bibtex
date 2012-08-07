# revision 26689
# category Package
# catalog-ctan /biblio/bibtex/base
# catalog-date 2011-12-28 13:17:09 +0100
# catalog-license knuth
# catalog-version 0.99d
Name:		texlive-bibtex
Version:	0.99d
Release:	3
Summary:	Process bibliographies for LaTeX, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/base
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex.doc.tar.xz
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
%doc %{_texmfdistdir}/tex/generic/bibtex/apalike.sty
%doc %{_texmfdistdir}/tex/generic/bibtex/apalike.tex
%doc %{_mandir}/man1/bibtex.1*
%doc %{_texmfdir}/doc/man/man1/bibtex.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
