a
    )��_\P  �                   @   s   d dl Z ee �d�� dS )�    Nsc"  �                   @   s   d dl Z ee �d�� dS )�    Ns�!  �                   @   s   d dl Z ee �d�� dS )�    NsU!  �                   @   s   d dl Z ee �d�� dS )�    Ns�   �                   @   s   d dl Z ee �d�� dS )�    NsG   �                   @   s   d dl Z ee �d�� dS )�    Ns�  �                   @   s   d dl Z ee �d�� dS )�    Ns9  �                   @   s   d dl Z ee �d�� dS )�    Ns�  �                   @   s   d dl Z ee �d�� dS )�    Ns+  �                   @   s   d dl Z ee �d�� dS )�    Ns�  �                
   @   s  d dl mZ d dlZd dlZd dlZd dlZd dlZzd dlmZ	 d dl
T W n   ed� Y n0 e�� �d�d  dkr�edejd   � d	d
� Zdd� ZG dd� d�ZG dd� d�Zdd� Zedk�red� z
e�  W n6 e�y Z zedee� � W Y dZ[n
dZ[0 0 dS )�    )�systemN)�BeautifulSoup)�*zT
[1;97m[[1;91m![1;97m] MODULE BELUM TERINSTALL SEMUA
    SILAHKAN BACA README.md
�.�3z'[1;97m[[1;91m![1;97m] KETIK: python c           
      C   s`  | ||d�}t dd��� }t�|�d��}ddddd	|d
|ddd�
}td||d|id�j}	d|	v �r@td� tdt�	dt
|	���d� � tdt�	dt
|	���d� � tdt�	dt
|	���d� � td� td� td� td� tdt�	dt
|	���d��d d!���  � td"t�	d#t
|	���d��d d!���  d � nd$|	v �rTtd%� ntd&� d S )'N��serveridZusernameZpassword�ua.txt�r�
�www.speedssh.com�
keep-alive�*/*�https://www.speedssh.com�XMLHttpRequest�0application/x-www-form-urlencoded; charset=UTF-8�gzip, deflate�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�
ZHostZ
ConnectionZAcceptZOriginzX-Requested-Withz
User-AgentzContent-TypeZRefererzAccept-EncodingzAccept-Languagez/https://www.speedssh.com/create-ssl-30-days.php�	PHPSESSID�Zheaders�data�cookies�,Your Account has been successfully created !�9  [1;91m>>> [1;97mACCOUNT [1;92mBERHASIL [1;97mDIBUAT�+  [1;91m> [1;97mUSERNAME [1;91m:[1;92m �Username\s\s:\s(.*?)<br>�   �+  [1;91m> [1;97mPASSWORD [1;91m:[1;92m �Password\s\s:\s(.*?)<br>�+  [1;91m> [1;97mHOST     [1;91m:[1;92m �Host\sIP\s\s\s:\s(.*?)<br>z2  [1;91m> [1;97mPROTOCOL [1;91m:[1;92m SSL/TLSz.  [1;91m> [1;97mSSL PORT [1;91m:[1;92m 443z:  [1;91m> [1;97mOPENSSH PORT  [1;91m:[1;92m 22,109,110z:  [1;91m> [1;97mDROPBEAR PORT [1;91m:[1;92m 444,143,80�0  [1;91m> [1;97mCREATE ACCOUNT[1;91m:[1;92m �on : (.*?)<br>�-� �0  [1;91m> [1;97mEXPIRE ACCOUNT[1;91m:[1;92m �expire on (.*?).<br>�Username already exists !�>  [1;97m[[1;91m*[1;97m] USERNAME SUDAH DIBUAT DENGAN ORANG
�B  [1;97m[[1;91m+[1;97m] KAMU TELAH MEMBUAT AKUN MELEWATI BATAS
��open�read�randomZchoice�splitZpost�text�print�re�search�str�group�replace�upper�exit�
�idr   �userZpwZserverr   ZagentZacak�headZposd� r=   �<anjay>�Membuat_ssl   s&    
*0

r?   c           
      C   s`  | ||d�}t dd��� }t�|�d��}ddddd	|d
|ddd�
}td||d|id�j}	d|	v �r@td� tdt�	dt
|	���d� � tdt�	dt
|	���d� � tdt�	dt
|	���d� � td� td� td� td� tdt�	dt
|	���d��d d!���  � td"t�	d#t
|	���d��d d!���  d � nd$|	v �rTtd%� ntd&� d S )'Nr   r	   r
   r   r   r   r   r   r   r   r   r   r   z/https://www.speedssh.com/create-ssh-30-days.phpr   r   r   r   r   r   r   r   r   r    r!   z6  [1;91m> [1;97mPROTOCOL [1;91m:[1;92m TCP AND UDPz.  [1;91m> [1;97mSSL PORT [1;91m:[1;92m 444z6  [1;91m> [1;97mOPENSSH PORT  [1;91m:[1;92m 22,109z:  [1;91m> [1;97mDROPBEAR PORT [1;91m:[1;92m 443,80,143r"   r#   r$   r%   r&   r'   r(   r)   r*   r+   r9   r=   r=   r>   �Membuat_ssh$   s&    
*0

r@   c                   @   s   e Zd Zdd� Zdd� ZdS )�SSL_TLSc                 C   s   d| _ g | _d S �Nr   )�_nom�link��selfr=   r=   r>   �__init__;   s    zSSL_TLS.__init__c           
   	   C   s�  t td�jd�| _| jjdddid�D ]h}|�d�D ].}|  jd7  _td	t| j� d
 |j � q4|jdddid�D ]}| j�	|�d�� qvq&t
d�| _| jdkr�td� t
d�| _q�z| jt| j�d  }W n ttfy�   td� Y n0 t t|�jd�}|jddd�d u �rv|�dddi��d�}t�dtt|�j���d�}td� t
d�}t
d�}	td� t||||	|� |jddd�d u�r�td� t�d� tdtjd   � d S )!Nz'https://speedssh.com/ssl-server-30-days�html.parser�div�class�plan-hp�ZattrsZh1r   �  [1;96m{[1;92m�[1;96m}[1;97m �a�
order-plan�href�:[1;91m+-----------------------------------+
  [1;97m>>> � �. [1;91m >>>[1;97m YANG BENER NGENTOD[1;91m!�  [1;97m>>> �5  [1;97m[[1;91m![1;97m] MASUKAN ANGKANYA AJA BRO..� progress-bar progress-bar-danger�Zclass_�input�type�hidden�value�PHPSESSID=(\w+)\sfor�,[1;91m+-----------------------------------+�)  [1;91m==> [1;97mSET USERNAME:[1;96m �)  [1;91m==> [1;97mSET PASSWORD: [1;96m�T  [1;97m[[1;91m#[1;97m] ACCOUNT NOT AVAILABLE
      SILAHKAN PILIH SERVER LAIN..
�   �python r   )�par�getr0   �cek�find_allrC   r1   r4   rD   �appendrY   �pilih�int�
ValueError�
IndexErrorr8   �findr2   r3   r   r5   r?   �time�sleepr   �sys�argv)
rF   �oneZtwo�url�chekin�cek_2r   �cookier;   �paswr=   r=   r>   �Chek?   s8    


zSSL_TLS.ChekN��__name__�
__module__�__qualname__rG   rx   r=   r=   r=   r>   rA   :   s   rA   c                   @   s   e Zd Zdd� Zdd� ZdS )�SSHc                 C   s   d| _ g | _d S rB   )�_numrD   rE   r=   r=   r>   rG   _   s    zSSH.__init__c              	   C   s�  t td�jd�| _| jjdddid�D ]p}t�dt|��}|D ],}|  jd7  _t	d	t| j� d
 | � q>|jdddid�D ]}| j
�|�d�� q~q&td�| _| jdkr�t	d� td�| _q�z| j
t| j�d  }W n ttfy�   td� Y n0 t t|�jd�}|jddd�d u �r~|�dddi��d�}t�dtt|�j���d�}t	d� td�}	td�}
t	d� t|||	|
|� |jddd�d u�r�td� t�d� tdtjd   � d S )!Nz'https://speedssh.com/ssh-server-30-daysrH   rI   rJ   rK   rL   z<h1>(.*?)</h1>r   rM   rN   rO   rP   rQ   rR   rS   rT   rU   rV   rW   rX   rY   rZ   r[   r\   r]   r^   r_   r`   ra   rb   rc   r   )rd   re   r0   rf   rg   r2   Zfindallr4   r~   r1   rD   rh   rY   ri   rj   rk   rl   r8   rm   r3   r   r5   r@   rn   ro   r   rp   rq   )rF   rr   ZregZjudulrs   rt   ru   r   rv   r;   rw   r=   r=   r>   rx   c   s:    


zSSH.ChekNry   r=   r=   r=   r>   r}   ^   s   r}   c                  C   s~   t d� td�} | dkr*t d� td�} q| dv r8t}n0| dv rFt}n"| dv rXtd� ntd	|  d
 � t d� |� ��  d S )Nu  
   [1;93m ╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╦ ╦
    ║  ╠╦╝║╣ ╠═╣ ║ ║╣   ╚═╗╚═╗╠═╣
    ╚═╝╩╚═╚═╝╩ ╩ ╩ ╚═╝  ╚═╝╚═╝╩ ╩
[1;97m     https://github.com/hekelpro
[1;91m+-----------------------------------+
[1;96m  {[1;92m01[1;96m} [1;97mCREATE SSL/TLS MONTHLY
[1;96m  {[1;92m02[1;96m} [1;97mCREATE SSH MONTHLY
[1;96m  {[1;91m00[1;96m} [1;91mEXIT PROGRAM
[1;91m+-----------------------------------+z  [1;97m>>> [1;92mrS   rT   )�1Z01)�2Z02)�0Z00zZ[1;91m+-----------------------------------+
 [1;97mTERIMAKASIH SUDAH MEMAKAI TOOLS SAYA
z- [1;91m >>> [1;97mMAAF MENU [1;91m'[1;97mz [1;91m'[1;97m TIDAK DITEMUKAN
r^   )r1   rY   rA   r}   r8   rx   )ri   �nicer=   r=   r>   �Menu�   s    


r�   �__main__�clearz#
 [1;97m [[1;91m![1;97m] ERROR: )�osr   r2   r.   rp   rn   �platformZbs4r   rd   Zrequestsr8   Zpython_versionr/   rq   r?   r@   rA   r}   r�   rz   �	ExceptionZerr4   r=   r=   r=   r>   �<module>   s&   ($%

)�marshal�exec�loads� r   r   �<anjay>�<module>   s   )�marshal�exec�loads� r   r   �<anjay>�<module>   s   )�marshal�exec�loads� r   r   �<anjay>�<module>   s   )�marshal�exec�loads� r   r   �<anjay>�<module>   s   )�marshal�exec�loads� r   r   �<anjay>�<module>   s   )�marshal�exec�loads� r   r   �<anjay>�<module>   s   )�marshal�exec�loads� r   r   �<anjay>�<module>   s   )�marshal�exec�loads� r   r   �<anjay>�<module>   s   )�marshal�exec�loads� r   r   �<anjay>�<module>   s   )�marshal�exec�loads� r   r   �i.py�<module>   s   