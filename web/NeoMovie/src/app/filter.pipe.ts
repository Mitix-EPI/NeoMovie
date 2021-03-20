import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filterSearch'
})
export class FilterPipe implements PipeTransform {
  transform(items: any[], searchText: string): any[] {
    if (!items) return [];
    if (!searchText) return items;

    return items.filter(item => {
        console.log(item[1], searchText);
        return String(item[1]).toLowerCase().includes(searchText.toLowerCase());
    });
   }
}
