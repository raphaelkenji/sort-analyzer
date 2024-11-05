# sort-analyzer
 
Esta é uma adaptação do projeto de Analisador Léxico e Sintático que eu fiz para a matéria de Compiladores (GCC1730) do Curso de Bacharelado em Ciência da Computação no Centro Federal de Educação Tecnológica Celso Suckow da Fonseca (CEFET/RJ) no período de 2024.1.

### Requisitos

```
ply
```

### Execução
Métodos de ordenação disponíveis:
- bubble_sort
- insertion_sort
- selection_sort
- merge_sort
- quick_sort
- heap_sort
```bash
py main.py
> compare [número] [algoritmos]; [compare [numero] [algoritmos]; ...]
```

### Árvore de Derivação
```javascript
<command>   ::= <entry> semicolon
            | <command>

<entry>     ::= compare number <formalgo>

<formalgo>  ::= algorithm
            | algorithm comma <formalgo>

<algorithm> ::= bubble_sort
            | insertion_sort
            | selection_sort
            | merge_sort
            | quick_sort
            | heap_sort
``` 
