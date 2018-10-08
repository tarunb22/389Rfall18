section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rax, rdi  ;send str to rax
        mov rcx, 0    ;i accumulator, set to 0
        mov r10, [rax + rdx]
    l1:
        cmp rcx, rdx  ;compare i and size
        jge l2        ;if i >= size then jump to l2
        mov [rax + rcx], rsi    ; add val to str
        inc rcx       ; increment accumulator
        jmp l1        ; go back to cmp
    l2:
        mov [rax + rcx], r10
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rax, rdi  ;send str to rax
        mov rcx, 0    ;i accumulator, set to 0
        mov r12, [rax + rdx]
    s1:
        cmp rcx, rdx  ;compare i and size
        jge s2        ;if i >= size then jump to l2
        mov r8, [rsi + rcx]   ;store src[i]
        mov [rax + rcx], r8  ;dst[i] = src[i]
        inc rcx       ; increment accumulator
        jmp s1        ; go back to cmp
    s2:
        mov [rax + rcx], r12
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
